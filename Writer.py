# -*- coding: utf-8 -*-
from moviepy.editor import *
from moviepy.video.fx.all import *
import ntpath
import logging
import time
import random

class Writer():
    '''Helper class to write video'''
    def __init__(self):
        self.counter = 5 #debugging option
        self.name = "_OUT.avi"

    def get_filename(self):
        head, tail = ntpath.split(self.path)
        return tail or ntpath.basename(head)

    def resize(self):
        '''writes only video, resizing it to 1920x1080 size'''
        try:
            for i, sequence in enumerate(self.sequences_video):
                self.sequences_video[i] = sequence.resize( (1920, 1080) )
        except Exception as NoVideoError:
            logging.info("Error occured, \n {}".format(NoVideoError))

    def write(self, clip):
        # clip.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30, codec='libx264', audio_codec='aac')
        clip.write_videofile("./output_video/" + self.get_filename() + self.date + self.name, codec='libx264')

    def write_video(self):
        self.name = '_OUT.avi'
        # if (hasattr(self, 'sequences_video')):
            # while (self.counter > 0):
        self.date = time.strftime("%I%M%S")
        self.resize() # ITS IMPORTANT!
        logging.debug("Chopped {} and altered {} sequences".format(self.sequences_video, self.sequences_altered))
        sequences_concatenated = self.sequences_video + self.sequences_altered
        logging.debug("Videos will be writed: {}".format(sequences_concatenated))
        clipOut = concatenate_videoclips(sequences_concatenated, method='compose')
        # self.clipOut.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.mp4", fps=30, codec='libx264', audio_codec='aac')
        self.write(clipOut)
        # except Exception as e:
            # self.counter -= 1
                    
        # else:
        #     logging.info("No video available for write")

    def wirte_video_separate(self):
        '''no audio for now'''
        self.name = "_SEPARATE.avi"
        # self.resize()
        sequences_shuffled = self.sequences_video + self.sequences_altered
        random.shuffle(sequences_shuffled)
        for clip in sequences_shuffled:
            self.date = time.strftime("%I%M%S")
            self.write(clip)

    def write_audio(self):
        '''writes only audio'''
        self.date = time.strftime("%I%M%S")
        clipOut = concatenate_audioclips(self.sequences_audio)
        clipOut.write_audiofile("./output_video/" + self.get_filename() + self.date + "-out.wav")

    def wirte_audio_separate(self):
        self.date = time.strftime("%I%M%S")
        while clip in self.sequences_audio:
            clip.write_videofile("./output_video/" + self.get_filename() + self.date + "-out.wav")

