import spacy
from django.core.files.storage import FileSystemStorage
from werkzeug.utils import secure_filename
from spacy.tokens import DocBin
from tqdm import tqdm
import uuid
import json
import pickle
import pandas as pd
import sys, fitz
import pathlib
import spacy_transformers
import os
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
path=os.getcwd()
UPLOAD_FOLDER = os.path.join(path,r"scrapper/datafiles")
MEDIA_UPLOAD_FOLDER = os.path.join(path, "media/")
ALLOWED_EXTENSIONS = {'docx', 'pdf', 'xlsx','csv','xls'}
RESUME_PARSER_MODEL = 'resume.pkl'


def spacy_model_function(file, resultAsDf = True):
    filename = secure_filename(file.name)
    fs = FileSystemStorage(location=UPLOAD_FOLDER) #defaults to   MEDIA_ROOT  
    fs.save(filename, file)
    # nlp.p is a pickle file where we stored the trained model
    best_model2 = pickle.load(open("C:/Users/Lenovo/Desktop/ResumeParser/resumeParser/scrapper/pklfile/resume.pkl","rb"))

    # add the input path in fname
    # fname = (os.path.join(UPLOAD_FOLDER,file_obj.file.name.split('/')[-1]))

    doc = fitz.open(os.path.join(UPLOAD_FOLDER, filename))
    #doc = fitz.open(file)
    text = " "
    for page in doc:
      text = text + str(page.get_text())


    text = text.strip()
    text = ' '.join(text.split())


    doc = best_model2(text)
    mylist = []
    for ent in doc.ents:
    #print(ent.label_, " : ",ent.text)
      mylist.append([ent.label_,ent.text])

    skill_list = []
    res = {'Skills':0}
    for i in mylist:
       if i[0] == 'SKILLS':
          skill_list.append(i[1])
    for sub in mylist:
      if sub[0] == 'SKILLS':
        res['Skills'] = skill_list
      else:
         res[sub[0]] = sub[1]
   # return json.dumps(mylist)
    return json.dumps(res)

