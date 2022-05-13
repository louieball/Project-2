from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx


# merges them
def clip_merge(clip_1, clip_2, name, c1_start, c1_end, c2_start, c2_end):
    clip1 = VideoFileClip(clip_1).subclip(c1_start, c1_end).fx(vfx.fadein, 0.5).fx(vfx.fadeout, 0.5)
    clip2 = VideoFileClip(clip_2).subclip(c2_start, c2_end).fx(vfx.fadein, 0.5).fx(vfx.fadeout, 0.5)
    combined = concatenate_videoclips([clip1, clip2])
    combined.write_videofile("{}.mp4".format(name))
