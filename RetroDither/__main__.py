from PIL import Image
from argparse import ArgumentParser
from RetroDither.dither import dither
from RetroDither.macpaint import MAX_WIDTH, MAX_HEIGHT, write_macpaint_file

def prepare(file_name: str) -> Image.Image:
	with open(file_name, "rb") as fp:
		image = Image.open(fp)
		# Size to within the bounds of the maximum for MacPaint
		if image.width > MAX_WIDTH or image.height > MAX_HEIGHT:
			desired_ratio = MAX_WIDTH / MAX_HEIGHT
			ratio = image.width / image.height 
			if ratio >= desired_ratio:
				new_size = (MAX_WIDTH, int(image.height * (MAX_WIDTH/ image.width)))
			else:
				new_size = (int(image.width * (MAX_HEIGHT / image.height)), MAX_HEIGHT)
			image.thumbnail(new_size, Image.Resampling.LANCZOS)
		# Convert to grayscale
		return image.convert("L")

if __name__ == "__main__":
	argument_parser = ArgumentParser("RetroDither")
	argument_parser.add_argument("image_file", help="Input image file.")
	argument_parser.add_argument("output_file", help="Resulting MacPaint file.")
	argument_parser.add_argument('-g', '--gif', default=False, action=='store_true',
								help='Create an output gif as well.')
	arguments = argument_parser.parse_args()
	original = prepare(arguments.image_file)
	dithered_data = dither(original)
	if arguments.gif:
		out_image = Image.frombytes('L', original.size, dithered_data.tobytes())
		out_image.save(arguments.output_file + ".gif")
	write_macpaint_file(dithered_data, arguments.output_file, original.width, original.height)
