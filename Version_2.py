import pyautogui as pg
import time

coords = {
    "start_solidx": 695,
    "start_solidy": 1063,
    "Start_filex": 218,
    "Start_filey": 16,
    "openx": 401,
    "openy": 372,
    "extrudex": 36,
    "extrudey": 89,
    "pl_selectx": 1003,
    "pl_selecty": 358,
    "cir_selectx": 162,
    "cir_selecty": 55,
    "clc_center": 1080,
    "clc_centery": 563,
    "rnd_pointx": 959,
    "rnd_pointy": 571,
    "smrt_dimx": 65,
    "smrt_dimy": 71,
    "clc_cirx": 954,
    "clc_ciry": 554,
    "rnd_pos_outx": 698,
    "rnd_pos_outy": 582,
    "confr_dimx": 777,
    "conft_dimy": 576,
    "chec_mrkx": 1829,
    "chec_mrky": 192,
    "clc_cir_othx": 958,
    "clc_cir_othy": 563,
    "clc_for_dimx": 129,
    "clc_for_dimy": 420,
    "endx": 1829,
    "endy": 192,
}

pg.click(coords["start_solidx"], coords["start_solidy"])
time.sleep(10)
pg.click(coords["Start_filex"], coords["Start_filey"])
time.sleep(2)
pg.click(coords["openx"], coords["openy"], clicks=2)
time.sleep(2)
pg.click(coords["extrudex"], coords["extrudey"])
time.sleep(3)
pg.click(coords["pl_selectx"], coords["pl_selecty"])
time.sleep(0.7)
pg.click(coords["cir_selectx"], coords["cir_selecty"])
time.sleep(1.3)
pg.click(coords["clc_center"], coords["clc_centery"])
time.sleep(1)
pg.click(coords["rnd_pointx"], coords["rnd_pointy"])
time.sleep(0.7)
pg.click(coords["smrt_dimx"], coords["smrt_dimy"])
time.sleep(0.7)
pg.click(coords["clc_cirx"], coords["clc_ciry"])
time.sleep(1)
pg.click(coords["rnd_pos_outx"], coords["rnd_pos_outy"])
time.sleep(1)
pg.typewrite("200")
time.sleep(0.2)
pg.typewrite(["enter"])
pg.click(coords["confr_dimx"], coords["conft_dimy"])
time.sleep(1)
pg.click(coords["chec_mrkx"], coords["chec_mrky"])
time.sleep(0.5)
pg.click(coords["extrudex"], coords["extrudey"])
time.sleep(0.5)
pg.click(coords["clc_cir_othx"], coords["clc_cir_othy"])
time.sleep(0.5)
pg.click(coords["clc_for_dimx"], coords["clc_for_dimy"])
time.sleep(0.5)
pg.typewrite(" + 40")
time.sleep(0.2)
pg.click(coords["endx"], coords["endy"])
