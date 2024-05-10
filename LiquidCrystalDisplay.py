# For more projects, visit www.micropythonforu.com

from machine import Pin
from time import sleep_ms
from time import sleep_us
from commands import *

class LCD:
    
    def __init__(self, rs, rw, enable, d0, d1, d2, d3, d4, d5, d6, d7):
        
        self.rs_pin = Pin(rs, Pin.OUT)
        self.enable_pin = Pin(enable, Pin.OUT)
        self.rw_pin = Pin(rw, Pin.OUT)
        
        self.databits = [0,0,0,0,0,0,0,0]
        
        self.databits[0] = Pin(d0, Pin.OUT)
        self.databits[1] = Pin(d1, Pin.OUT)
        self.databits[2] = Pin(d2, Pin.OUT)
        self.databits[3] = Pin(d3, Pin.OUT)
        self.databits[4] = Pin(d4, Pin.OUT)
        self.databits[5] = Pin(d5, Pin.OUT)
        self.databits[6] = Pin(d6, Pin.OUT)
        self.databits[7] = Pin(d7, Pin.OUT)
        
        sleep_ms(100)
        self.rs_pin.off()
        self.rw_pin.off()
        self.enable_pin.off()
        
        sleep_ms(100)
 
    def send_enable_pulse(self):
        self.enable_pin.off()
        sleep_us(10)
        self.enable_pin.on()
        sleep_us(40)
        self.enable_pin.off()
        sleep_us(10)
    

    def write8bits(self, byte):
        #print("Writing CMD =",hex(byte))
        sleep_ms(100)
        for i in range(8):
            self.databits[i].value( (byte >> i) & 0x01)
        self.send_enable_pulse()
        
    def write4bits(self, byte):
        #print("Writing CMD =",hex(byte))
        sleep_ms(100)
        for i in range(4):
            self.databits[i].value( (byte >> i) & 0x01)
        self.send_enable_pulse()
 
    def set_config(self, bit_mode, dot_type, num_of_lines):  
        if (bit_mode == 4):
            self.display_config = LCD_4BITMODE | LCD_5x8DOTS | LCD_1LINE
        else:
            self.display_config = LCD_8BITMODE | LCD_5x8DOTS | LCD_1LINE
            
        if (num_of_lines > 1):
            self.display_config = self.display_config | LCD_2LINE
            
    def lcd_init(self):
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(50)
        
        #Set Display, Cursor and Blicking On
        cmd = LCD_DISPLAYCONTROL | LCD_DISPLAYON | LCD_CURSORON | LCD_BLINKON
        self.write8bits(cmd)
        sleep_us(50)
        
    def clear(self):
        cmd = LCD_CLEARDISPLAY
        self.write8bits(cmd)
        sleep_us(500)
        
    def home(self):
        cmd = LCD_RETURNHOME
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_display_on(self):
        self.display_config = self.display_config & LCD_DISPLAYOFF
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_display_off(self):
        self.display_config = self.display_config & LCD_DISPLAYON
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_cursor_on(self):
        display_config = self.display_config & LCD_CURSORON
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_cursor_off(self):
        self.display_config = self.display_config & LCD_CURSOROFF
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_blink_off(self):
        print(hex(self.display_config))
        self.display_config = -LCD_BLINKOFF
        print(hex(self.display_config))
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)
        
    def set_blink_on(self):
        self.display_config = self.display_config & LCD_BLINKON
        cmd = self.display_config | LCD_FUNCTIONSET
        self.write8bits(cmd)
        sleep_us(500)

    def show_text(self, string):
        self.rs_pin.on()
        for i in range(len(string)):
            self.write8bits(int(hex(ord(string[i]))))
        sleep_ms(50)
        self.rs_pin.off()
        
    def scrollDisplayLeft(self):
        cmd = LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVELEFT
        self.write8bits(cmd)
        sleep_us(500)
        
    def scrollDisplayRight(self):
        cmd = LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT
        self.write8bits(cmd)
        sleep_us(500)
        
    def leftToRight(self):
        cmd = LCD_CURSORSHIFT | LCD_DISPLAYMOVE | LCD_MOVERIGHT
        self.write8bits(cmd)
        sleep_us(500)       
        

