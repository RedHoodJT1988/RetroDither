# RetroDither

🎨 **RetroDither**: Bringing Old-School Dithering Back to the Future!

Ever wondered how your favorite 80s and 90s computer graphics got that pixel-perfect, retro look? **RetroDither** is here to sprinkle some vintage magic on your modern images! Whether you want to relive the glory days of MacPaint or just make your photos look like they belong on a floppy disk, this Python project has you covered.

## Features

- 🖼️ **Classic Dithering Algorithms** – From error diffusion to MacPaint-style, we’ve got your pixels covered.
- ⚡ **Fast & Easy** – Just a few lines of code to retro-fy your images.
- 🕹️ **Nostalgia Overload** – Perfect for game devs, artists, and anyone who misses the sound of dial-up.

## Installation

Clone this repo and make sure you have Python 3.7+ installed:

```bash
git clone https://github.com/yourusername/RetroDither.git
cd RetroDither
```

Install dependencies (if any):

```bash
pip install -r requirements.txt  # (if you have one)
```

## Usage

You can run RetroDither from the command line or import it into your own Python scripts:

```bash
python -m RetroDither input_image.png output_image.png
```

Or use it in your code:

```python
from dither import retro_dither
retro_dither('input.png', 'output.png')
```

## Testing

We love tests almost as much as we love pixels! Run them with:

```bash
pytest tests/
```

## Contributing

Pull requests, bug reports, and new dithering algorithms are always welcome. Bonus points for puns in your commit messages.

## License

MIT – Because sharing is caring.

---

*RetroDither: Because every pixel deserves a little nostalgia.*
