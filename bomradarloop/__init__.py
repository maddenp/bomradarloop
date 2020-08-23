"""
Provides animated GIF images of weather-radar imagery derived the Australian
Bureau of Meteorology (http://www.bom.gov.au/australia/radar/).
"""

import datetime as dt
import io
import logging
import os
import time

import PIL.Image
import requests

# Legend:
#
# NSW: http://www.bom.gov.au/australia/radar/nsw_radar_sites_table.shtml
#  NT: http://www.bom.gov.au/australia/radar/nt_radar_sites_table.shtml
# QLD: http://www.bom.gov.au/australia/radar/qld_radar_sites_table.shtml
#  SA: http://www.bom.gov.au/australia/radar/sa_radar_sites_table.shtml
# TAS: http://www.bom.gov.au/australia/radar/tas_radar_sites_table.shtml
# VIC: http://www.bom.gov.au/australia/radar/vic_radar_sites_table.shtml
#  WA: http://www.bom.gov.au/australia/radar/wa_radar_sites_table.shtml
#
# res: 1 => 512km, 2 => 256km, 3 => 128km, 4 => 64km

# fmt: off
RADARS = {
    "Adelaide":        {"id": "64", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Adelaide (Buckland Park) [SA]
    "Albany":          {"id": "31", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Albany [WA]
    "AliceSprings":    {"id": "25", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Alice Springs [NT]
    "Bairnsdale":      {"id": "68", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Bairnsdale [VIC]
    "Bowen":           {"id": "24", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Bowen [QLD]
    "Brisbane":        {"id": "66", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Brisbane (Mt Stapylton) [QLD]
    "Broome":          {"id": "17", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Broome [WA]
    "Cairns":          {"id": "19", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Cairns [QLD]
    "Canberra":        {"id": "40", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Canberra (Captains Flat) [NSW]
    "Carnarvon":       {"id": "05", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Carnarvon [WA]
    "Ceduna":          {"id": "33", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Ceduna [SA]
    "Dampier":         {"id": "15", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Dampier [WA]
    "Darwin":          {"id": "63", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Darwin (Berrimah) [NT]
    "Emerald":         {"id": "72", "delta": 600, "frames": 4, "res": (1, 2, 3, 4)}, # Emerald [QLD]
    "Esperance":       {"id": "32", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Esperance [WA]
    "Geraldton":       {"id": "06", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Geraldton [WA]
    "Giles":           {"id": "44", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Giles [WA]
    "Gladstone":       {"id": "23", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Gladstone [QLD]
    "Gove":            {"id": "09", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Gove [NT]
    "Grafton":         {"id": "28", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Grafton [NSW]
    "Gympie":          {"id": "08", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Gympie (Mt Kanigan) [QLD]
    "HallsCreek":      {"id": "39", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Halls Creek [WA]
    "Hobart":          {"id": "76", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Hobart (Mt Koonya) [TAS]
    "Kalgoorlie":      {"id": "48", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Kalgoorlie [WA]
    "Katherine":       {"id": "42", "delta": 360, "frames": 6, "res": (1, 2, 3)},    # Katherine (Tindal) [NT]
    "Learmonth":       {"id": "29", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Learmonth [WA]
    "Longreach":       {"id": "56", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Longreach [QLD]
    "Mackay":          {"id": "22", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Mackay [QLD]
    "Marburg":         {"id": "50", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Brisbane (Marburg) [QLD]
    "Melbourne":       {"id": "02", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Melbourne [VIC]
    "Mildura":         {"id": "30", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Mildura [VIC]
    "Moree":           {"id": "53", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Moree [NSW]
    "MorningtonIs":    {"id": "36", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Gulf of Carpentaria (Mornington Is) [QLD]
    "MountIsa":        {"id": "75", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Mount Isa [QLD]
    "MtGambier":       {"id": "14", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Mt Gambier [SA]
    "Namoi":           {"id": "69", "delta": 600, "frames": 4, "res": (1, 2, 3, 4)}, # Namoi (Blackjack Mountain) [NSW]
    "Newcastle":       {"id": "04", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Newcastle [NSW]
    "Newdegate":       {"id": "38", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Newdegate [WA]
    "NorfolkIs":       {"id": "62", "delta": 600, "frames": 4, "res": (1, 2, 3, 4)}, # Norfolk Island [ET]
    "NWTasmania":      {"id": "52", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # N.W. Tasmania (West Takone) [TAS]
    "Perth":           {"id": "70", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Perth (Serpentine) [WA]
    "PortHedland":     {"id": "16", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Pt Hedland [WA]
    "Rainbow":         {"id": "95", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Rainbow [VIC]
    "SellicksHill":    {"id": "46", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Adelaide (Sellicks Hill) [SA]
    "SouthDoodlakine": {"id": "58", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # South Doodlakine [WA]
    "Sydney":          {"id": "71", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Sydney (Terrey Hills) [NSW]
    "Townsville":      {"id": "73", "delta": 600, "frames": 4, "res": (1, 2, 3, 4)}, # Townsville (Hervey Range) [QLD]
    "WaggaWagga":      {"id": "55", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Wagga Wagga [NSW]
    "Warrego":         {"id": "67", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Warrego [QLD]
    "Warruwi":         {"id": "77", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Warruwi [NT]
    "Watheroo":        {"id": "79", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Watheroo [WA]
    "Weipa":           {"id": "78", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Weipa [QLD]
    "WillisIs":        {"id": "41", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Willis Island [QLD]
    "Wollongong":      {"id": "03", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Wollongong (Appin) [NSW]
    "Woomera":         {"id": "27", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Woomera [SA]
    "Wyndham":         {"id": "07", "delta": 600, "frames": 4, "res": (1, 2, 3)},    # Wyndham [WA]
    "Yarrawonga":      {"id": "49", "delta": 360, "frames": 6, "res": (1, 2, 3, 4)}, # Yarrawonga [VIC]
}
# fmt: on

DEFAULT_RESOLUTION = "3"


class BOMRadarLoop:

    """
    The class to be instantiated by Home Assistant
    """

    def __init__(self, location=None, radar_id=None, delta=None, frames=None, outfile=None, logger=None):
        self._log = logger or logging.getLogger(__name__)
        if isinstance(radar_id, int):
            radar_id = "%03d" % radar_id
        valids = ", ".join(sorted(RADARS.keys()))
        if not radar_id and location not in RADARS:
            location = "Sydney"
            self._log.error("Bad 'location' specified, using '%s' (valid locations are: %s)", location, valids)
        if radar_id:
            if location in RADARS:
                radar_id = None
                self._log.error("Valid 'location' specified, ignoring 'radar_id'")
            elif location:
                self._log.error("Bad 'location' specified, using ID %s (valid locations are: %s)", radar_id, valids)
        if radar_id and not delta:
            delta = 360
            self._log.error("No 'delta' specified for radar ID %s, using %s", radar_id, delta)
        if radar_id and not frames:
            frames = 6
            self._log.error("No 'frames' specified for radar ID %s, using %s", radar_id, frames)
        self._location = location or "ID %s" % radar_id
        self._delta = delta or RADARS[location]["delta"]
        self._frames = frames or RADARS[location]["frames"]
        self._radar_id = radar_id or "%s%s" % (RADARS[location]["id"], DEFAULT_RESOLUTION)
        self._outfile = outfile
        self._t0 = 0
        self._current = self.current

    # Public methods

    @property
    def current(self):
        """
        Return the current BOM radar-loop image.
        """
        now = int(time.time())
        t1 = now - (now % self._delta)
        if t1 > self._t0:
            self._t0 = t1
            self._current = self._get_loop()
        return self._current

    # Private methods

    def _get_background(self):
        """
        Fetch the background map, then the topography, locations (e.g. city
        names), and distance-from-radar range markings, and merge into a single
        image.
        """
        self._log.debug("Getting background for %s at %s", self._location, self._t0)
        suffix0 = "products/radar_transparencies/IDR%s.background.png"
        url0 = self._get_url(suffix0 % self._radar_id)
        background = self._get_image(url0)
        if background is None:
            return None
        for layer in ("topography", "locations", "range"):
            self._log.debug("Getting %s for %s at %s", layer, self._location, self._t0)
            suffix1 = "products/radar_transparencies/IDR%s.%s.png" % (self._radar_id, layer)
            url1 = self._get_url(suffix1)
            image = self._get_image(url1)
            if image is not None:
                try:
                    background = PIL.Image.alpha_composite(background, image)
                except ValueError:
                    pass
        return background

    def _get_frames(self):
        """
        Fetch a radar image for each expected time, composite it with a common
        background image, then overlay on the legend to produce a frame. Collect
        and return the frames, ignoring any blanks. If no frames were produced,
        return None (the caller must expect this).
        """
        self._log.debug("Getting frames for %s at %s", self._location, self._t0)
        bg = self._get_background()
        legend = self._get_legend()
        frames = []
        if bg and legend:
            for time_str in self._get_time_strs():
                fg = self._get_wximg(time_str)
                if fg is not None:
                    frames.append(legend.copy())
                    frames[-1].paste(PIL.Image.alpha_composite(bg, fg), (0, 0))
        return frames

    def _get_image(self, url):  # pylint: disable=no-self-use
        """
        Fetch an image from the BOM.
        """
        self._log.debug("Getting image %s", url)
        response = requests.get(url)
        if response.status_code == 200:
            log_level = self._log.level
            self._log.setLevel(logging.INFO)
            image = PIL.Image.open(io.BytesIO(response.content))
            rgba_img = image.convert("RGBA")
            image.close()
            self._log.setLevel(log_level)
            return rgba_img
        return None

    def _get_legend(self):
        """
        Fetch the BOM colorbar legend image.
        """
        self._log.debug("Getting legend at %s", self._t0)
        url = self._get_url("products/radar_transparencies/IDR.legend.0.png")
        return self._get_image(url)

    def _get_loop(self):
        """
        Return an animated GIF comprising a set of frames, where each frame
        includes a background, one or more supplemental layers, a colorbar
        legend, and a radar image.
        """
        self._log.info("Getting loop for %s at %s", self._location, self._t0)
        loop = io.BytesIO()
        frames = self._get_frames()
        if frames:
            self._log.debug("Got %s frames for %s at %s", len(frames), self._location, self._t0)
            frames[0].save(
                loop, append_images=frames[1:], duration=500, format="GIF", loop=0, save_all=True,
            )
        else:
            self._log.warning("Got NO frames for %s at %s", self._location, self._t0)
            PIL.Image.new("RGB", (512, 557)).save(loop, format="GIF")
        if self._outfile:
            outdir = os.path.dirname(self._outfile)
            if not os.path.isdir(outdir):
                try:
                    os.makedirs(outdir)
                except OSError:
                    self._log.error("Could not create directory %s", outdir)
            try:
                with open(self._outfile, "wb") as outfile:
                    outfile.write(loop.getvalue())
            except IOError:
                self._log.error("Could not write image to %s", self._outfile)
        return loop.getvalue()

    def _get_time_strs(self):
        """
        Return a list of strings representing YYYYMMDDHHMM times for the most
        recent set of radar images to be used to create the animated GIF. The
        timestamps on 512km-resolution radar-loop images are offset from those
        of the other resolutions by -1 hour for every-6-minutes (delta=360)
        radars, and -3 minutes for every-10-minutes (delta=600) radars, so
        compensate for this fact when producing time strings for 512km loops.
        """
        self._log.debug("Getting time strings starting at %s", self._t0)
        if len(self._radar_id) != 3:
            raise ValueError("Radar ID must be 3 digits")
        resolution = {1: 512, 2: 256, 3: 128, 4: 64}[int(self._radar_id[-1])]
        offset = {360: 5, 600: 7}.get(self._delta, 0) * 60 if resolution == 512 else 0
        tz = dt.timezone.utc
        f = lambda n: dt.datetime.fromtimestamp(self._t0 + offset - (self._delta * n), tz=tz).strftime("%Y%m%d%H%M")
        frame_numbers = range(self._frames, 0, -1)
        return [f(n) for n in frame_numbers]

    def _get_url(self, path):  # pylint: disable=no-self-use
        self._log.debug("Getting URL for path %s", path)
        return "http://www.bom.gov.au/%s" % path

    def _get_wximg(self, time_str):
        """
        Return a radar weather image from the BOM website. Note that
        get_image() returns None if the image could not be fetched, so the
        caller must deal with that possibility.
        """
        self._log.debug("Getting radar imagery for %s at %s", self._location, time_str)
        suffix = "radar/IDR%s.T.%s.png" % (self._radar_id, time_str)
        url = self._get_url(suffix)
        return self._get_image(url)
