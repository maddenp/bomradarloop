"""
Test bomradarloop by downloading all resolutions of all known-active radars.
"""

import logging
import os
import time

import bomradarloop

EXCLUDE = [
    "15",  # Dampier offline as of 2020-08-23
]

radars = {
    v["id"]: {"delta": v["delta"], "frames": v["frames"], "res": v["res"]}
    for _, v in bomradarloop.RADARS.items()
    if v["id"] not in EXCLUDE
}

logging.Formatter.converter = time.gmtime
logging.basicConfig(
    format="[%(asctime)s] %(levelname)s %(message)s", datefmt="%Y-%m-%dT%H:%M:%SZ", level=logging.DEBUG,
)
logger = logging.getLogger()
outdir = "gifs"
os.makedirs(outdir, exist_ok=True)
for base_id, props in radars.items():
    for res in props["res"]:
        radar_id = "%s%s" % (base_id, res)
        outfile = os.path.join(outdir, "%s.gif" % radar_id)
        logger.info("Composing %s", outfile)
        bomradarloop.BOMRadarLoop(
            location=None, radar_id=radar_id, delta=props["delta"], frames=props["frames"], outfile=outfile, logger=logger,
        )
