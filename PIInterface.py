import epd7in5_V2
import logging

class PI:
    def print(image):
        try:
            epd = epd7in5_V2.EPD()
            logging.info("init")
            self.epd.init()
            self.epd.display(epd.getbuffer(image))
            logging.info("Goto Sleep...")
            self.epd.sleep()

        except IOError as e:
            logging.info(e)

        except KeyboardInterrupt:
            logging.info("ctrl + c:")
            epd7in5_V2.epdconfig.module_exit()
            exit()
