import torch
from run import main
from PIL import Image

#@markdown `image` is a path and can be a URL or a local file (or blank)
image =  'https://guillaumejaume.github.io/FUNSD/img/form_example.png' #@param {type:"string"}
if len(image)==0:
    image=None

show_output_mask = False #@param {type:"boolean"}

checkpoint = 'dessurt_docvqa_best.pth'

main(checkpoint,None,image,None,False,default_task_token='natural_q~',dont_output_mask=not show_output_mask)