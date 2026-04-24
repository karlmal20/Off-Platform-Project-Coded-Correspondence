def caesar_decoded(message, offset):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  decoded_message = ''
  for letter in message:
    if letter in alpha:
      index = alpha.index(letter)
      new_index = (index + offset) % 26
      decoded_message += alpha[new_index]
    else: 
      decoded_message += letter
  return decoded_message
def caesar_encode(message, offset):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  decoded_message2 = ''
  for letter in message:
    if letter in alpha:
      index = alpha.index(letter)
      new_index = (index - offset)%26
      decoded_message2 += alpha[new_index]
    else:
      decoded_message2 += letter
  return decoded_message2
Vishal_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!' 
alpha = 'abcdefghijklmnopqrstuvwxyz'
decoded_message = ''
for letter in Vishal_message:
  if letter in alpha:
    index = alpha.index(letter)
    new_index = (index + 10) % 26
    decoded_message += alpha[new_index]
  else: 
    decoded_message += letter
print(decoded_message)
my_message = 'Hey, how are you?'
decoded_message2 = ''
for letter in my_message:
  if letter in alpha:
    index = alpha.index(letter)
    new_index = (index - 10)%26
    decoded_message2 += alpha[new_index]
  else:
    decoded_message2 += letter
print(decoded_message2)
Vishal_reply1 = 'jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.'
Vishal_reply2 = 'bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!'
print(caesar_decoded(Vishal_reply1, 10))
print(caesar_decoded(Vishal_reply2, 14))
Vishal_letter = 'vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px\'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.'
print(caesar_decoded(Vishal_letter, 7))
Vishal_letter2 =  'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!'
decoded_message3 = ''
keyword_message = ''
keyword_index = 0
keyword = 'friends'
for letter in Vishal_letter2:
  if letter in alpha:
    letter_index = alpha.index(letter)
    key_index = alpha.index(keyword[keyword_index % len(keyword)])
    new_index = (letter_index + key_index) % 26
    decoded_message3 += alpha[new_index]
    keyword_index += 1
  else:
    decoded_message3 += letter
print(decoded_message3)






