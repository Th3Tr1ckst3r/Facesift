"""
    Facesift - A lightweight, cross-platform, & accurate Python3 image sorter with facial recognition capabilities.
    Created by Adrian Tarver(Th3Tr1ckst3r) @ https://github.com/Th3Tr1ckst3r/

////////////////////////////////////////////////////////////////////////////////////////

  IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.

  By downloading, copying, installing, or using the software you agree to this license.
  If you do not agree to this license, do not download, install,
  copy, or use the software.


                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  Developers that use our General Public Licenses protect your rights
with two steps: (1) assert copyright on the software, and (2) offer
you this License which gives you legal permission to copy, distribute
and/or modify the software.

  A secondary benefit of defending all users' freedom is that
improvements made in alternate versions of the program, if they
receive widespread use, become available for other developers to
incorporate.  Many developers of free software are heartened and
encouraged by the resulting cooperation.  However, in the case of
software used on network servers, this result may fail to come about.
The GNU General Public License permits making a modified version and
letting the public access it on a server without ever releasing its
source code to the public.

  The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version.

  An older license, called the Affero General Public License and
published by Affero, was designed to accomplish similar goals.  This is
a different license, not a version of the Affero GPL, but Affero has
released a new version of the Affero GPL which permits relicensing under
this license.

  The precise terms and conditions for copying, distribution and
modification follow here:

https://raw.githubusercontent.com/Th3Tr1ckst3r/Facesift/main/LICENSE

"""
import sys
import os
import shutil
import face_recognition
import magic
import argparse
from PIL import Image


def get_face(img_path=None):
    try:
        image = face_recognition.load_image_file(img_path)
        face_landmarks_list = face_recognition.face_landmarks(image)
        if face_landmarks_list:
            return True
        else:
            return False
    except:
        return False


def compare_faces(known_image_encoding=None, unknown_image_path=None):
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces([known_image_encoding], unknown_encoding)
    return results[0]


def detect_filetype(file_path=None):
    f = magic.Magic(mime=True)
    mime_type = f.from_file(file_path)
    return str(mime_type)


def load_image(image_path=None):
    if os.path.exists(image_path):
        file_type = detect_filetype(image_path)
        if 'image' in file_type:
            img = Image.open(image_path)
            return img
        else:
            return False
    else:
        print('\n\nError: Please provide valid filepath, & file type.')
        sys.exit(1)


def validate_path(path=None):
    dir = os.path.dirname(path)
    if not dir:
        print("\n\nError: Directory is not specified.")
        return False
    if not os.path.isdir(dir):
        print(f"\n\nError: Directory '{path}' does not exist.")
        return False
    if not os.path.isabs(path):
        print("\n\nError: Output path must be an absolute path.")
        return False
    return True


def main():
    known_image = None
    known_image_encoding = None
    parser = argparse.ArgumentParser(prog='facesift.py',
                                     description="Facesift V1.0 - A lightweight, cross-platform, & accurate Python3 image sorter with facial recognition capabilities.", epilog='For more help, please visit:  https://github.com/Th3Tr1ckst3r/Facesift')
    parser.add_argument('--input_image', type=str, default=None, help='Input image for Facesift to use for the purpose of either matching, or differentiating.')
    parser.add_argument('--input_dir', type=str, default=None, help='Input directory for Facesift to parse through.')
    parser.add_argument('--output_dir', type=str, default=None, help='Output directory to place matching, or differentiating images into.')
    parser.add_argument('--match_face', action='store_true', default=False, help='Enables face matching using an input image.')
    parser.add_argument('--diff_face', action='store_true', default=False, help='Enables differentiating face matching using an input image.')
    parser.add_argument('--verbose', '-v', action='store_true', default=False, help='Enables verbosity within Facesift.')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1) 
    if not args.input_image:
        print("\n\n[Error]: A valid input image is required in order to get any real use out of Facesift.")
        sys.exit(1)
    if args.input_image:
        img = load_image(args.input_image)
        if img is False:
            print("\n\n[Error]: The input image provided does not contain valid image data.")
            sys.exit(1)
        else:
            has_face = get_face(args.input_image)
            if has_face:
                input_image_valid = True
                known_image = face_recognition.load_image_file(args.input_image)
                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                if args.verbose:
                    print("\n\n[Info]: Input image was accepted by Facesift as input for facial recognition.")
                else:
                    pass
            else:
                print("\n\n[Error]: The input image provided does not contain a human face that can be detected.")
                sys.exit(1)
    if args.output_dir:
        is_valid = validate_path(args.output_dir)
        if is_valid:
            if args.verbose:
                print("\n\n[Info]: Output directory provided has been accepted by Facesift.")
            else:
                pass
        else:
            print("\n\n[Error]: The output directory is invalid.")
            sys.exit(1)
    if args.input_dir:
        is_valid = validate_path(args.input_dir)
        if is_valid:
            if args.verbose:
                print("\n\n[Info]: Input directory provided has been accepted by Facesift.")
            else:
                pass
        else:
            print("\n\n[Error]: The output directory is invalid.")
            sys.exit(1)
    if args.match_face:
        for dirpath, dirnames, filenames in os.walk(args.input_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                has_face = get_face(file_path)
                if has_face:
                    result = compare_faces(known_image_encoding, file_path)
                    if result:
                        if args.output_dir:
                            shutil.move(file_path, args.output_dir)
                        else:
                            print("\n\nPath contains a matching face: {0}".format(file_path))
                            continue
                    else:
                        continue
                else:
                    continue
        if args.output_dir:
            print("Positive matching results were saved to: {0}".format(args.output_dir))
        sys.exit(1)
    else:
        for dirpath, dirnames, filenames in os.walk(args.input_dir):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                has_face = get_face(file_path)
                if has_face:
                    result = compare_faces(known_image_encoding, file_path)
                    if result == False:
                        if args.output_dir:
                            shutil.move(file_path, args.output_dir)
                        else:
                            print("\n\nPath contains a differentiating face: {0}".format(file_path))
                            continue
                    else:
                        continue
                else:
                    continue
        if args.output_dir:
            print("Differentiating results were saved to: {0}".format(args.output_dir))
        sys.exit(1)


if __name__ == "__main__":
    main()
    sys.exit(1)

