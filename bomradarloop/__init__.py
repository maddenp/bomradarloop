import datetime as dt
import io
import logging
import multiprocessing.dummy
import os
import time

import PIL.Image
import requests

RADARS = {
    'Adelaide':        {'id': '643', 'delta': 360, 'frames': 6},
    'Albany':          {'id': '313', 'delta': 600, 'frames': 4},
    'AliceSprings':    {'id': '253', 'delta': 600, 'frames': 4},
    'Bairnsdale':      {'id': '683', 'delta': 600, 'frames': 4},
    'Bowen':           {'id': '243', 'delta': 600, 'frames': 4},
    'Brisbane':        {'id': '663', 'delta': 360, 'frames': 6},
    'Broome':          {'id': '173', 'delta': 600, 'frames': 4},
    'Cairns':          {'id': '193', 'delta': 360, 'frames': 6},
    'Canberra':        {'id': '403', 'delta': 360, 'frames': 6},
    'Carnarvon':       {'id': '053', 'delta': 600, 'frames': 4},
    'Ceduna':          {'id': '333', 'delta': 600, 'frames': 4},
    'Dampier':         {'id': '153', 'delta': 600, 'frames': 4},
    'Darwin':          {'id': '633', 'delta': 360, 'frames': 6},
    'Emerald':         {'id': '723', 'delta': 600, 'frames': 4},
    'Esperance':       {'id': '323', 'delta': 600, 'frames': 4},
    'Geraldton':       {'id': '063', 'delta': 600, 'frames': 4},
    'Giles':           {'id': '443', 'delta': 600, 'frames': 4},
    'Gladstone':       {'id': '233', 'delta': 600, 'frames': 4},
    'Gove':            {'id': '093', 'delta': 600, 'frames': 4},
    'Grafton':         {'id': '283', 'delta': 600, 'frames': 4},
    'Gympie':          {'id': '083', 'delta': 360, 'frames': 6},
    'HallsCreek':      {'id': '393', 'delta': 600, 'frames': 4},
    'Hobart':          {'id': '763', 'delta': 360, 'frames': 6},
    'Kalgoorlie':      {'id': '483', 'delta': 360, 'frames': 6},
    'Katherine':       {'id': '423', 'delta': 360, 'frames': 6},
    'Learmonth':       {'id': '293', 'delta': 600, 'frames': 4},
    'Longreach':       {'id': '563', 'delta': 600, 'frames': 4},
    'Mackay':          {'id': '223', 'delta': 600, 'frames': 4},
    'Marburg':         {'id': '503', 'delta': 600, 'frames': 4},
    'Melbourne':       {'id': '023', 'delta': 360, 'frames': 6},
    'Mildura':         {'id': '303', 'delta': 600, 'frames': 4},
    'Moree':           {'id': '533', 'delta': 600, 'frames': 4},
    'MorningtonIs':    {'id': '363', 'delta': 600, 'frames': 4},
    'MountIsa':        {'id': '753', 'delta': 360, 'frames': 6},
    'MtGambier':       {'id': '143', 'delta': 600, 'frames': 4},
    'Namoi':           {'id': '693', 'delta': 600, 'frames': 4},
    'Newcastle':       {'id': '043', 'delta': 360, 'frames': 6},
    'Newdegate':       {'id': '383', 'delta': 360, 'frames': 6},
    'NorfolkIs':       {'id': '623', 'delta': 600, 'frames': 4},
    'NWTasmania':      {'id': '523', 'delta': 360, 'frames': 6},
    'Perth':           {'id': '703', 'delta': 360, 'frames': 6},
    'PortHedland':     {'id': '163', 'delta': 600, 'frames': 4},
    'SellicksHill':    {'id': '463', 'delta': 600, 'frames': 4},
    'SouthDoodlakine': {'id': '583', 'delta': 360, 'frames': 6},
    'Sydney':          {'id': '713', 'delta': 360, 'frames': 6},
    'Townsville':      {'id': '733', 'delta': 600, 'frames': 4},
    'WaggaWagga':      {'id': '553', 'delta': 600, 'frames': 4},
    'Warrego':         {'id': '673', 'delta': 600, 'frames': 4},
    'Warruwi':         {'id': '773', 'delta': 360, 'frames': 6},
    'Watheroo':        {'id': '793', 'delta': 360, 'frames': 6},
    'Weipa':           {'id': '783', 'delta': 360, 'frames': 6},
    'WillisIs':        {'id': '413', 'delta': 600, 'frames': 4},
    'Wollongong':      {'id': '033', 'delta': 360, 'frames': 6},
    'Woomera':         {'id': '273', 'delta': 600, 'frames': 4},
    'Wyndham':         {'id': '073', 'delta': 600, 'frames': 4},
    'Yarrawonga':      {'id': '493', 'delta': 360, 'frames': 6},
}


class BOMRadarLoop:

    def __init__(self, location=None, radar_id=None, delta=None, frames=None, outfile=None, logger=None):

        self._log = logger or logging.getLogger(__name__)

        if isinstance(radar_id, int):
            radar_id = '%03d' % radar_id

        valids = ', '.join(sorted(RADARS.keys()))

        if not radar_id and location not in RADARS:
            location = 'Sydney'
            self._log.info("Bad 'location' specified, using '%s' (valid locations are: %s)", location, valids)
        if radar_id:
            if location in RADARS:
                radar_id = None
                self._log.info("Valid 'location' specified, ignoring 'radar_id'")
            elif location:
                self._log.info("Bad 'location' specified, using ID %s (valid locations are: %s)", radar_id, valids)
        if radar_id and not delta:
            delta = 360
            self._log.info("No 'delta' specified for radar ID %s, using %s", radar_id, delta)
        if radar_id and not frames:
            frames = 6
            self._log.info("No 'frames' specified for radar ID %s, using %s", radar_id, frames)

        self._location = location or 'ID %s' % radar_id
        self._delta = delta or RADARS[location]['delta']
        self._frames = frames or RADARS[location]['frames']
        self._radar_id = radar_id or RADARS[location]['id']
        self._outfile = outfile

        self._t0 = 0
        self._current = self.current

    # Public methods

    @property
    def current(self):
        '''
        Return the current BOM radar-loop image.
        '''
        now = int(time.time())
        t1 = now - (now % self._delta)
        if t1 > self._t0:
            self._t0 = t1
            self._current = self._get_loop()
        return self._current

    # Private methods

    def _get_background(self):
        '''
        Fetch the background map, then the topography, locations (e.g. city
        names), and distance-from-radar range markings, and merge into a single
        image.
        '''
        self._log.info('Getting background for %s at %s', self._location, self._t0)
        suffix0 = 'products/radar_transparencies/IDR%s.background.png'
        url0 = self._get_url(suffix0 % self._radar_id)
        background = self._get_image(url0)
        if background is None:
            return None
        for layer in ('topography', 'locations', 'range'):
            self._log.info('Getting %s for %s at %s', layer, self._location, self._t0)
            suffix1 = 'products/radar_transparencies/IDR%s.%s.png' % (self._radar_id, layer)
            url1 = self._get_url(suffix1)
            image = self._get_image(url1)
            if image is not None:
                background = PIL.Image.alpha_composite(background, image)
        return background

    def _get_frames(self):
        '''
        Use a thread pool to fetch a set of current radar images in parallel,
        then get a background image for this location, combine it with the
        colorbar legend, and finally composite each radar image onto a copy of
        the combined background/legend image.

        The 'wximages' list is created so that requested images that could not
        be fetched are excluded, so that the set of frames will be a best-
        effort set of whatever was actually available at request time. If the
        list is empty, None is returned; the caller can decide how to handle
        that.
        '''
        self._log.info('Getting frames for %s at %s', self._location, self._t0)
        pool0 = multiprocessing.dummy.Pool(self._frames)
        raw = pool0.map(self._get_wximg, self._get_time_strs())
        wximages = [x for x in raw if x is not None]
        if not wximages:
            return None
        pool1 = multiprocessing.dummy.Pool(len(wximages))
        background = self._get_background()
        if background is None:
            return None
        composites = pool1.map(lambda x: PIL.Image.alpha_composite(background, x), wximages)
        legend = self._get_legend()
        if legend is None:
            return None
        frames = pool1.map(lambda _: legend.copy(), composites)
        pool1.map(lambda x: x[0].paste(x[1], (0, 0)), zip(frames, composites))
        return frames

    def _get_image(self, url): # pylint: disable=no-self-use
        '''
        Fetch an image from the BOM.
        '''
        self._log.info('Getting image %s', url)
        response = requests.get(url)
        if response.status_code == 200:
            image = PIL.Image.open(io.BytesIO(response.content))
            return image.convert('RGBA')
        return None

    def _get_legend(self):
        '''
        Fetch the BOM colorbar legend image.
        '''
        self._log.info('Getting legend at %s', self._t0)
        url = self._get_url('products/radar_transparencies/IDR.legend.0.png')
        return self._get_image(url)

    def _get_loop(self):
        '''
        Return an animated GIF comprising a set of frames, where each frame
        includes a background, one or more supplemental layers, a colorbar
        legend, and a radar image.
        '''
        self._log.info('Getting loop for %s at %s', self._location, self._t0)
        loop = io.BytesIO()
        frames = self._get_frames()
        if frames is not None:
            self._log.info('Got %s frames for %s at %s', len(frames), self._location, self._t0)
            frames[0].save(loop, append_images=frames[1:], duration=500, format='GIF', loop=0, save_all=True)
        else:
            self._log.info('Got NO frames for %s at %s', self._location, self._t0)
            PIL.Image.new('RGB', (512, 557)).save(loop, format='GIF')
        if self._outfile:
            outdir = os.path.dirname(self._outfile)
            if not os.path.isdir(outdir):
                try:
                    os.makedirs(outdir)
                except OSError:
                    self._log.error('Could not create directory %s', outdir)
            try:
                with open(self._outfile, 'wb') as outfile:
                    outfile.write(loop.getvalue())
            except IOError:
                self._log.error('Could not write image to %s', self._outfile)
        return loop.getvalue()

    def _get_time_strs(self):
        '''
        Return a list of strings representing YYYYMMDDHHMM times for the most
        recent set of radar images to be used to create the animated GIF.
        '''
        self._log.info('Getting time strings starting at %s', self._t0)
        frame_numbers = range(self._frames, 0, -1)
        tz = dt.timezone.utc
        f = lambda n: dt.datetime.fromtimestamp(self._t0 - (self._delta * n), tz=tz).strftime('%Y%m%d%H%M')
        return [f(n) for n in frame_numbers]

    def _get_url(self, path): # pylint: disable=no-self-use
        self._log.info('Getting URL for path %s', path)
        return 'http://www.bom.gov.au/%s' % path

    def _get_wximg(self, time_str):
        '''
        Return a radar weather image from the BOM website. Note that
        get_image() returns None if the image could not be fetched, so the
        caller must deal with that possibility.
        '''
        self._log.info('Getting radar imagery for %s at %s', self._location, time_str)
        suffix = '/radar/IDR%s.T.%s.png' % (self._radar_id, time_str)
        url = self._get_url(suffix)
        return self._get_image(url)
