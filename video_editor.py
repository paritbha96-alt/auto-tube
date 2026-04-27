import moviepy.editor as mp

class VideoEditor:
    def __init__(self):
        pass

    def combine_audio_video(self, video_file, audio_file, output_file):
        # Load video and audio files
        video_clip = mp.VideoFileClip(video_file)
        audio_clip = mp.AudioFileClip(audio_file)

        # Set audio to the video
        final_clip = video_clip.set_audio(audio_clip)

        # Write the final video file
        final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

    def apply_effects(self, video_file, output_file, effects):
        # Load video file
        video_clip = mp.VideoFileClip(video_file)

        # Apply effects
        for effect in effects:
            if effect == 'fadein':
                video_clip = video_clip.fadein(1)  # 1 second fade-in
            elif effect == 'fadeout':
                video_clip = video_clip.fadeout(1)  # 1 second fade-out

        # Write the final video file
        video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

# Example usage
# editor = VideoEditor()
# editor.combine_audio_video('video.mp4', 'audio.mp3', 'final_video.mp4')
# editor.apply_effects('final_video.mp4', 'final_video_with_effects.mp4', ['fadein', 'fadeout'])
