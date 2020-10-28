from vedo import settings as vsettings

# ------------------------------- vedo settings ------------------------------ #

vsettings.pointSmoothing = False
vsettings.lineSmoothing = False
vsettings.polygonSmoothing = False


# For transparent background with screenshots
vsettings.screenshotTransparentBackground = True  # vedo for transparent bg
vsettings.useFXAA = False  # This needs to be false for transparent bg


# --------------------------- brainrender settings --------------------------- #

DEFAULT_ATLAS = "allen_mouse_25um"  # default atlas
WHOLE_SCREEN = True  # If true render window is full screen
BACKGROUND_COLOR = "white"
SHOW_AXES = True
DEFAULT_CAMERA = "three_quarters"  # Default camera settings (orientation etc. see brainrender.camera.py)
ROOT_COLOR = [0.8, 0.8, 0.8]  # color of the overall brain model's actor
ROOT_ALPHA = 0.2  # transparency of the overall brain model's actor'
SHADER_STYLE = "cartoon"  # affects the look of rendered brain regions: [metallic, plastic, shiny, glossy]
SCREENSHOT_SCALE = 1
HDF_SUFFIXES = [".h5", ".hdf", ".hdf5", ".he5"]
DEFAULT_HDF_KEY = "hdf"
INTERACTIVE = True
LW = 2
