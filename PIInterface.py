import epd7in5_V2
import logging

logging.info("init")
epd = epd7in5_V2.EPD()

def printOut(image):
    try:        
        epd.init()
        epd.display(epd.getbuffer(image))
        logging.info("Goto Sleep...")
        epd.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd7in5_V2.epdconfig.module_exit()
        exit()
