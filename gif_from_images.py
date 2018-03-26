import imageio
import glob

file_extensions = ('jpg', 'png')


def get_files(folder):
    # gets a list of files from the given folder with specified file extension
    return [file for file in glob.glob(''.join([folder, '\*.*'])) if file.lower().endswith(file_extensions)]


def create_gif(duration, input_location,  output_file):
    files = get_files(input_location)
    images = []

    # reading all the image files
    for filename in files:
        images.append(imageio.imread(filename))
    # saving gif file in the py file location
    imageio.mimsave(output_file, images, duration=duration)


dur = input('What is the duration of each frame? ')
input_folder = input('What is the path to the folder with input images? ')
output_name = input('What is the name of the output file? ')

create_gif(int(dur), input_folder, output_name)
