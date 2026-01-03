from moviepy import VideoFileClip
from rich.console import Console

console = Console()

def convert_video_to_gif(video_path, gif_path, start_time=0, duration=None):
    console.rule("Uploading the original video")
    console.print(f"[blue bold]VIDEO: {video_path}[/blue bold]")

    clip = VideoFileClip(video_path)

    console.rule("Clipping to duration if Duration is not NONE")

    if duration:
        clip = clip.subclipped(start_time, start_time + duration)
    else:
        clip = clip.subclipped(start_time, clip.duration)

    # If we do not RESIZE nor do the below optimizations in `write_gif()` we 
    # end up with a big ass gif video! e.g. from 800kb -> 15mb (OJO)

    clip = clip.resized(width=1080) # This still produces a big ass gif, ~16mb or so

    console.rule("Writing the optimized GIF video")

    clip.write_gif(
        gif_path,               
        fps=12,                     # Lower FPS (10-15 is usually enough for GIFs)
        loop=2,
    )
    
    console.print(f"[red bold]GIF Video saved to {gif_path}[/red bold]")

def main():
    video_path = "./assets/test_video.mp4"
    gif_path = "./assets/test_video.gif"

    convert_video_to_gif(video_path, gif_path)


if __name__ == '__main__':
    main()
