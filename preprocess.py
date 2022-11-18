import argparse
import text
from utils import load_filepaths_and_text

# if __name__ == '__main__':
#   parser = argparse.ArgumentParser()
#   parser.add_argument("--out_extension", default="cleaned")
#   parser.add_argument("--text_index", default=1, type=int)
#   parser.add_argument("--filelists", nargs="+", default=["filelists/ljs_audio_text_val_filelist.txt", "filelists/ljs_audio_text_test_filelist.txt"])
#   parser.add_argument("--text_cleaners", nargs="+", default=["english_cleaners2"])

#   args = parser.parse_args()
    
#   for filelist in args.filelists:
#     print("START:", filelist)
#     filepaths_and_text = load_filepaths_and_text(filelist)
#     for i in range(len(filepaths_and_text)):
#       original_text = filepaths_and_text[i][args.text_index]
#       cleaned_text = text._clean_text(original_text, args.text_cleaners)
#       filepaths_and_text[i][args.text_index] = cleaned_text

#     new_filelist = filelist + "." + args.out_extension
#     with open(new_filelist, "w", encoding="utf-8") as f:
#       f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])

out_extension = "cleaned"
text_index = 1
filelists = ["filelists/ljs_audio_text_val_filelist.txt", "filelists/ljs_audio_text_test_filelist.txt"]
text_cleaners = ["english_cleaners2"]

for filelist in filelists:
  print("START:", filelist)
  filepaths_and_text = load_filepaths_and_text(filelist)
  for i in range(len(filepaths_and_text)):
    original_text = filepaths_and_text[i][text_index]
    cleaned_text = text._clean_text(original_text, text_cleaners)
    filepaths_and_text[i][text_index] = cleaned_text

  new_filelist = filelist + "." + out_extension
  with open(new_filelist, "w", encoding="utf-8") as f:
    f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])


