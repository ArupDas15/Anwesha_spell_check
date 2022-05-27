from random import random, choice
from random import *
from helper import _preprocess_terms,_parse_into_words
SameClusterDict = {
    'অ' : ['ও'],
    'আ' : ['আ'],
    'ই':['ই'],
    'ঈ':['ই'],
    'উ' : ['উ'],
    'ঊ' : ['উ'],
    'ঋ' : ['রি'],
    'এ' : ['এ'],
    'ঐ': ['অই'],
    'ও': ['ও'],
    'ঔ': ['অউ'],
    
    'ক': ['ক'],
    'খ': ['ক'],
    'গ': ['গ'],
    'ঘ ': ['গ'],
    'ঙ': ['◌ং'],
    'চ': ['চ'],
    'ছ': ['চ'],
    'জ': ['জ'],
    'ঝ': ['জ'],
    'ঞ': ['ঞ'],
    'ট' : ['ত'],
    'ঠ' : ['ট','ত'],
    'ড' : ['দ'],
    'ঢ': ['ড','দ'],
    'ণ': ['ন'],
    'ত' : ['ত','ট'],
    'থ': ['ত','ট'],
    'দ' : ['দ','ড'],
    'ধ' : ['দ','ড'],
    'ন': ['ন'],
    'প' : ['প'],
    'ফ' : ['ফ'],
    'ব' : ['ব'],
    'ভ' : ['ব'],
    'ম' : ['ম'],
    'য' : ['জ'],
    'র' : ['র'],
    'ল' : ['ল'],
    'শ' : ['শ'],
    'ষ' : ['শ'],
    'স' : ['স'],
    '‍হ': ['হ'],
    'ড়' : ['র'],
    '‍ঢ়': ['র'],
    '‍য় ': ['য় '],

    'ৎ' : ['ত'],
    'ং' : ['ঙ'],
    'ঃ': ['হ'],
    '‍ঁ' : [''],

    '‍ি': ['ি'],
    'ী' : ['ি'],
    'ে':['ে'],
    'ৈ'  :['ই'],
    'ো' : ['ো'],
    'ৌ':['উ'],
    'ৃ' : ['রি'],
     '◌ূ'  : [' ু'],
     ' ু'  : ['◌ূ']
}
#Phonetic Similar Cluster Replacement
def SameClusterFun(c):
  if c in SameClusterDict:
    c2 = choice(SameClusterDict[c])
    print(c2,end='')
  else:
    print(c,end='')

#Single Letter Mispressed Cluster Replacement
ReplaceDict = {
      'ক' : ['ল','য'],
      'খ' : ['কগ','কজ','লহ','ঝ'],
      'গ' : ['ফ','হ'],
      'ঘ' : ['ফগ','হজ'],
      'ঙ' : ['ব','ম'],
      'চ' : ['ভ','চজ','চগ','ভহ'],
      'ছ' : ['ভ','চজ','চগ','ভহ'],
      'জ' : ['ক','হ'],
      'ঝ' : ['কজ','হগ'],
      'ট' : ['র'],
      'ঠ' : ['তজ','তগ','রহ'],
      'ড' : ['স','ফ'],
      'ঢ' : ['দজ','দ্গ','শ','ফহ'],
      'ণ' : ['ব','ম'],
      'ত' : ['র'],
      'থ' : ['তজ', 'তগ', 'রহ'],
      'দ' : ['স', 'ফ'],
      'ধ' : ['দজ', 'দ্গ', 'শ' ,'ফহ'],
      'ন' : ['ব','ম'],
      'প' : ['ও',' ো'],
      'ফ' : ['দ','গ'],
      'ব' : ['ভ','ন'],
      'ভ' : ['‍ব','চ'],
      'ম' : ['ন'],
      'য' : ['হ','ক'],
      'র' : ['এ',' ে','ত'],
      'ল' : ['ক'],
      'শ' : ['সজ','সগ','আহ','ঢ'],
      'ষ' : ['সজ','সগ','আহ','ঢ'],
      'স' : ['আ',' া','দ'],
      'হ' : ['গ','য'],
      'য়' : ['ত','উ','ু'],
      'ড়' : ['এ',' ে','ত'],
      'ঢ়' : ['এ',' ে','ত'],
      'ৎ' : ['র'],
      'ং' : ['ব','ম'],
      'ঃ' : ['গ','য'],
      'অ' : ['প',' ি','ই'],
      'আ' : ['স'],
      'ই' : ['উ','অ'],
      'ঈ' : ['উ','অ'],
      'উ' : ['ই',' ি'],
      'ঊ' : ['ই',' ি'],
      'ঋ' : [''],
      'এ' : ['ও','র'],
      'ঐ' : [''],
      'ও' : ['প','ই'],
      'ঔ' : [''],
      'া' : ['স'],
      'ি' : ['উ','অ'],
      'ো' : ['প',' ি'],
      'ৌ' : [''],
      'ে' : ['ো','র'],
      'ৈ' : ['']
    }

def ReplacementFun(c):
  if c in ReplaceDict:
    c2 = choice(ReplaceDict[c])
    print(c2,end='')
  else:
    print(c,end='')
JuktakkhorList = [' ক্ট ' , ' ক্ক ' , ' ক্ত ' , ' ক্য ' , ' ক্র ' , ' ক্ল ' , ' ক্ষ ' , ' ক্ষ্ণ ' , ' ক্ষ্ম ' , ' ক্ষ্য ' , ' ক্স ' , ' খ্র ' , ' গ্ধ ' , ' গ্ধ্য ' , ' গ্ন ' , ' গ্ন্য ' , ' গ্ব ' , ' গ্র ' , ' গ্র্য ' , ' গ্ল ' , ' ঘ্ন ' , ' ঘ্র ' , ' ঙ্ক্য ' , ' ঙ্গ্য ' , ' চ্চ ' , ' চ্ছ্ব ' , ' চ্য ' , ' জ্জ ' , ' জ্জ্ব ' , ' ট্ট ' , ' জ্ব ' , ' জ্য ' , ' জ্র ' , ' ট্য ' , ' ট্র ' , ' ড্ড ' , ' ড্র ' , ' ণ্ট ' , ' ণ্ঠ ' , ' ণ্ড ' , ' ণ্ণ ' , ' ণ্য ' , ' ৎক ' , ' ৎখ ' , ' ত্ত ' , ' ত্ত্ব ' , ' ত্ত্য ' , ' ত্ন ' , ' ৎপ ' , ' ত্ব ' , ' ত্ম ' , ' ত্ম্য ' , ' ত্য ' , ' ত্র ' , ' ত্র্য ' , ' ৎস ' , ' দ্ঘ ' , ' দ্দ ' , ' দ্ধ ' , ' দ্ব ' , ' দ্ভ ' , ' দ্ভ্র ' , ' দ্ম ' , ' দ্য ' , ' দ্র ' , ' দ্র্য ' , ' ধ্ব ' , ' ধ্য ' , ' ধ্র ' , ' ন্ট ' , ' ন্ট্র ' , ' ন্ঠ ' , ' ন্ড ' , ' ন্ড্র ' , ' ন্ত ' , ' ন্ত্ব ' , ' ন্ত্য ' , ' ন্ত্র ' , ' ন্ত্র্য ' , ' ন্থ ' , ' ন্দ ' , ' ন্দ্ব ' , ' ন্দ্র ' , ' ন্ধ ' , ' ন্ন ' , ' ন্য ' , ' প্ট ' , ' প্ত ' , ' প্ন ' , ' প্প ' , ' প্য ' , ' ব্দ ' , ' ব্ধ ' , ' ব্ব ' , ' ব্র ' , ' ভ্য ' , ' ভ্র ' , ' ম্প্র ' , ' ম্ব ' , ' ম্ম ' , ' ম্য ' , ' ম্র ' , ' য্য ' , ' র্ক ' , ' র্গ্য ' , ' র্ঘ্য ' , ' র্জ্য ' , ' র্থ্য ' , ' র্ব্য ' , ' র্খ ' , ' র্গ ' , ' র্ঘ ' , ' র্চ ' , ' র্ছ ' , ' র্জ ' , ' র্ঝ ' , ' র্ট ' , ' র্ড ' , ' র্ণ ' , ' র্ত ' , ' র্থ ' , ' র্দ ' , ' র্দ্ব ' , ' র্দ্র ' , ' র্ধ ' , ' র্ধ্ব ' , ' ল্ট ' , ' ল্ড ' , ' ল্প ' , ' ল্ম ' , ' ল্য ' , ' ল্ল ' , ' শ্ছ ' , ' শ্ন ' , ' শ্ব ' , ' শ্র ' , ' শ্ল ' , ' ষ্ক ' , ' ষ্ক্র ' , ' ষ্ট ' , ' ষ্ট্য ' , ' ষ্ট্র ' , ' ষ্ঠ ' , ' ষ্প ' , ' স্ট ' , ' স্ট্র ' , ' স্ত্র ' , ' স্ত ' , ' স্থ্য ' , ' স্য ' , ' স্র ' , ' স্ল ' , ' হ্র ' , ' হ্ল ' , ' গ্ম ' , ' ম্ভ ' , ' স্ম ' , ' ঙ্ঘ ' , ' ঙ্ক্ষ ' , ' ঙ্খ ' , ' ঙ্ক ' , ' ঙ্‌ক্ত ' , ' ঞ্চ ' , ' ঞ্ছ ' , ' ঞ্জ ' , ' হ্ন ' , ' ঙ্গ ' , ' জ্ঞ ' , ' গ্য ' , ' চ্ছ ' , ]

#Juktakkhor-handling-rules
def JuktoBorno(word,pos):  
  if word[pos] == 'জ' and word[pos+2] == 'ঞ':
    if pos == 0:
      print("গ",end='')
    else:
      print("জ্ঞ",end='')
  elif word[pos] == 'গ' and word[pos+2] == 'য':
    if pos == 0:
      print("গা",end='')
    else:
      print("জ্ঞ",end='')
  elif word[pos] == 'চ' and word[pos+2] == 'ছ':
    r = random()
    if r < .5:
      print("ছছ",end='')
    else:
      print("ছ",end='')
  elif word[pos+2] == 'য':
    if pos+2 == len(word):
      print(word[pos],end='')
      print(word[pos],end='')
    else:
      r = random()
      if r < .5:
        print(word[pos],end='')
        print("া",end='')
      else:
        print("ে",end='')
        print(word[pos],end='')
  elif word[pos] == 'স' and word[pos+2] == 'ম':
    SameClusterFun(word[pos])
  elif word[pos] == 'দ' and word[pos+2] == 'ম':
    SameClusterFun(word[pos])
    SameClusterFun(word[pos])
  elif word[pos] == 'ম':
    SameClusterFun(word[pos+2])
  elif word[pos+2] == 'ম':
    SameClusterFun(word[pos])
  elif word[pos] == 'ব':
    print(word[pos+2],end='')
  elif word[pos+2] == 'ব':
    print(word[pos],end='')
  elif word[pos] == 'র':
    print(word[pos],end='')
    SameClusterFun(word[pos+2])
  elif word[pos+2] == 'র':
    SameClusterFun(word[pos])
    print(word[pos+2],end='')
  elif word[pos] == 'ক' and word[pos+2] == 'ষ':
    if pos == 0:
      print("খ",end='')
    else:
      print("ক্ক",end='')
  elif word[pos+2] == 'ঙ':
    if word[pos+3] == "া" :
      SameClusterFun(word[pos])
      print("ঙ্গা",end='')
    else:
      SameClusterFun(word[pos])
      print("ং",end='')
  elif word[pos] == 'ঙ':
    print("ং",end='')
    SameClusterFun(word[pos+2])
  elif word[pos] == 'ঞ':
    print("ঞ",end='')
    SameClusterFun(word[pos+2])
  elif word[pos] == 'হ' and word[pos+2] == 'ন':
    print("ন্ন",end='')
  elif word[pos] == 'ন' and word[pos+2] == 'ন':
    print("হ্ন",end='')
  elif word[pos] == word[pos+2]:
    SameClusterFun(word[pos+2])
    SameClusterFun(word[pos+2])
  elif word[pos] == 'ল' or word[pos] == 'ত' or word[pos] == 'থ' or word[pos] == 'দ' or word[pos] == 'ধ' or word[pos] == 'ট' or word[pos] == 'ঠ' or word[pos] == 'স' or word[pos] == ' শ' or  word[pos] == 'ষ':
    print(word[pos],end='')
    SameClusterFun(word[pos+2])
  elif word[pos+2] == 'ল' or word[pos+2] == 'ত' or word[pos+2] == 'থ' or word[pos+2] == 'দ' or word[pos+2] == 'ধ' or word[pos+2] == 'ট' or word[pos+2] == 'ঠ' or word[pos+2] == 'স' or word[pos+2] == ' শ' or  word[pos+2] == 'ষ':
    SameClusterFun(word[pos])
    print(word[pos+2],end='')
  elif word[pos] == 'ন' or word[pos] == 'ণ':
    SameClusterFun(word[pos])
    SameClusterFun(word[pos+2])
  elif word[pos+2] == 'ন' or word[pos+2] == 'ণ':
    SameClusterFun(word[pos])
    SameClusterFun(word[pos+2])
  else:
    print(word[pos],end='')
    print(word[pos+1],end='')
    print(word[pos+2],end='')

NewWord = ""

def MakeError(word):
  nlist = []
  pos=0
  flag1=0
  flag2=0
  flag3=0
  while(pos<len(word)):
    if flag1 == 1 and flag2 == 1 and flag3 == 1:
      print(word[pos],end='')
      nlist.append(word[pos])
      pos += 1
    else:
      if(pos+1<len(word) and word[pos+1] == '্'):
        r = random()
        if r <= 1 and flag1 == 1:
          print(word[pos],end='')
          nlist.append(word[pos])
          print(word[pos+1],end='')
          nlist.append(word[pos+1])
          print(word[pos+2],end='')
          nlist.append(word[pos+2])
          pos=pos+3
        else:
          flag1=1
          error = 1
          JuktoBorno(word,pos)
          pos=pos+3
      else:
        r = random()
        #Same Cluster
        if r > 1:
          error = 1
          flag2=1
          SameClusterFun(word[pos])
        #Replacement
        elif r>1 and r<=.3:
          if flag3 == 1:
            print(word[pos],end='')
            nlist.append(word[pos])
          else:
            flag3=1
            error = 1
            ReplacementFun(word[pos])
        else:
          print(word[pos],end='')
          nlist.append(word[pos])
        pos+=1
  return nlist

def listToString(s):  
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  

InsertDict = {
    'ক': ['ল'],
    'খ': ['গ'],
    'গ' : ['ফ','হ'], 
    'ঘ' : ['জ'],
    'ঙ' : ['ম'],
    'চ' : ['জ'],
    'ছ' : ['জ'],
    'জ' : ['ক'],
    'ঝ' : ['গ'],
    'ট' : ['র'],
    'ঠ' : ['জ'],
    'ড' : ['স'],
    'ঢ' : ['জ'],
    'ণ' : ['ম'],
    'ত' : ['র'],
    'থ' : ['জ'],
    'দ' : ['স'],
    'ধ' : ['জ'],
    'ন' : ['ম'],
    'প' : [''],
    'ফ' : ['দ'],
    'ব' : ['ন'],
    'ম' : [''],
    'য' : ['ক'],
    'র' : ['ে'],
    'ল' : [''],
    'শ' : ['জ'],
    'ষ' : ['জ'],
    'স' : ['া'],
    'হ' : ['জ'],
    'য়' : ['ু'],
    'ড়' : ['ে'],
    'ঢ়' : ['ে'],
    'ৎ' : ['র'],
    'ং' : ['ম'],
    'ঃ' : ['জ'],
    'অ' : ['প'],
    'আ' : [''],
    'ই' : ['অ'],
    'ঈ' : ['অ'],
    'উ' : ['ি'],
    'ঊ' : ['ি'],
    'ঋ' : ['ো'],
    'এ' : ['ও'],
    'ঐ' : ['ু'],
    'ও' : ['প'],
    'ঔ' : ['য়'],
             }

character = ['অ','আ','ই','ঈ','উ','ঊ','এ','ঐ','ও','ঔ','ঋ','ঃ','ং','ৎ'
             'ক','খ','গ','ঘ','ঙ','চ', 'ছ','য','জ', 'ঝ','ট','ঠ','ড','র','ড়','ঢ়',
             'ণ','ত','থ','দ','ধ','ন','প','ফ','ব','ভ','ম','স','শ','ষ','য়','হ']
def lenth(words):
  l=0
  for i in words:
    if i in character:
      l += 1
  return l

def insert(word2):
  c = choice(word2)
  if c in InsertDict:
    position = word2.index(c)
    c2 = choice(InsertDict[c])
    return c2,position+1
  else:
    return insert(word2)

def insertChar(mystring, position, chartoinsert ):
    longi = len(mystring)
    mystring   =  mystring[:position] + chartoinsert + mystring[position:] 
    return mystring

def InsertionWord(word2):
  #print()
  #print(word2,end=',')
  if lenth(word2) > 2:
    element,index = insert(word2)
    word2 = insertChar(word2, index, element)
    print(word2)
  else:
    print(word2)




def main():

    bn =  open('bn_data.txt','r',encoding='utf-8')
    lines = bn.readlines()
    bn.close()

    tokens = _parse_into_words(" ".join(lines))
    preprocessed_tokens = _preprocess_terms(tokens)


    from contextlib import redirect_stdout

    with open('wrong_spell_new_list.txt', 'w') as f:
        with redirect_stdout(f):

            for token in preprocessed_tokens:
                if token == 'বৃহত্':
                    continue
                print(token,end=" ")
                nlist = MakeError(token)
                print()
                NewWord = listToString(nlist)
                #InsertionWord(NewWord)


if __name__ == "__main__":
    main()
