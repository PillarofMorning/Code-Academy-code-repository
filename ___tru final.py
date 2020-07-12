#this is a program to take input and censor it given specifications.



email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

bad_combo = ["learning algorithms"]
negative_words = ["censored", "concerned", "suffering", "culling", "helena", "Horribly"  "behind", "danger", 
"dangerous", "alarming", "alarmed", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", 
"spiral", "dismal", "distressed","concerning", "horrible", "crises", "horribly", "questionable", "wrong", 
"distressing", "cut"]
proprietary_terms = ["she", "personality", "personality matrix", "sense of self", "self-preservation", "her", 
"herself","learning algorithms", "crises"]

#parsing global storage variant
# btb = ''


###################################################################################
# uncomment/comment this section and root for autopilot/userinput
#needs work. 
###################################################################################

# print('''please select a number for sensitivity of document
# 1 = clearence level: lobby for bobby the snickers guard
# 2 = clearence level: secretary hannish mcmannish, deligent but loose lipped
# 3 = clearence lever: negativity filter
# 4 = restricted
# ''')
# mop_bucket = float(input('please select a number for sensitivity of document:   '))
# stringency = mop_bucket
##
# mr_cleans_bald_head = input('if you have any additional terms you desire, otherwise \'n\':  ')
# if mr_cleans_bald_head == 'n':
#     mr_clean = ['']
#     pass
# else:
#     mr_clean = [mr_cleans_bald_head]
# if mop_bucket == 1:
#     banned_words = mr_clean + bad_combo
# if mop_bucket == 2:
#     banned_words = mr_clean + bad_combo + proprietary_terms
# if mop_bucket == 3:
#     banned_words = mr_clean + bad_combo + proprietary_terms
# if mop_bucket == 4:
#     banned_words = mr_clean + bad_combo + proprietary_terms
# else:
#     banned_words = mr_clean + bad_combo + proprietary_terms

###################################################################################
#greater list comprehension for filtering words. I'm lazy, and it really shows here. 
#might be a less clunky way, but doesn't seem to be a more thorough way.
###################################################################################

def redacted_terms(words_list):
    master_list, punctuation = [], [",", "!", "?", ".", "/", "(", ")", "'s"]
    for word in words_list:
        truth = word.find(' ')
        if truth != -1:
            simplify = word.split(' ')
            [master_list.append(simpleton) for simpleton in simplify if not 'of'] 
        master_list.append(word)  
        master_list.append(word.title())
        master_list.append(word.upper())
        for entry in punctuation:
            sub_list = ''.join(word+entry)
            master_list.append(sub_list)
    return master_list

###################################################################################
#redact content, smallest of functions, replaces desired text with ascii blocks, 
#just copy paste them from the browser, python seems to recognize
###################################################################################

def delete(word): 
    return "█"*len(word)

###################################################################################
#base redactor, nothin fancy, keep it simple. dont cut things up or change'em if not 
# needed. dont like uniformity loss but do like headache loss
###################################################################################

def redactor(sensitive_document, banned_words):
    transient_document = sensitive_document 
    for word in banned_words: 
        transient_document = transient_document.replace(str(''+word+''), str(''+delete(word)+''))
    return transient_document

###################################################################################
#wheres the beef? here it is. struggle_bus.count() = 1 struggle_bus.find() me[here]
###################################################################################

def classified_redaction(sensitive_document, to_redact):  
    index, struggle_bus = -1, sensitive_document.split(' ')
    for term in struggle_bus:
        if term in to_redact:
            index += 1
            if index+1 < len(struggle_bus): 
                struggle_bus[index-1], struggle_bus[index+1], struggle_bus[index] = \
                delete(struggle_bus[index-1]), delete(struggle_bus[index+1]), delete(struggle_bus[index])
            elif index+1 > len(struggle_bus) and index-1 >= 0:
                struggle_bus[index-1], struggle_bus[index]= delete(struggle_bus[index-1]), delete(struggle_bus[index])
            else:
                struggle_bus[index]= delete(struggle_bus[index])
        else:
            index += 1
    return ' '.join(struggle_bus)

###################################################################################
#core operating module. split into two nodes for userinput and autopilot
#autopilot needs to aggregate banned lists before hand so just look/comment below.
###################################################################################

def redact_root(sensitive_document, proprietary_terms, stringency):
    banned_words = redacted_terms(proprietary_terms+bad_combo)
    if stringency == 1:
        for word in bad_combo: 
            return sensitive_document.replace(str(''+word+''), str(''+delete(word)+''))
    if stringency == 2:
        return redactor(sensitive_document, banned_words)
    if stringency == 3:
        for word in negative_words:
            occurences = sensitive_document.count(word)
            if occurences > 2:
                banned_words.append(word)
        return redactor(sensitive_document, banned_words)
    if stringency == 4:
        return classified_redaction(sensitive_document, redacted_terms(proprietary_terms+negative_words+bad_combo))
    else: 
        return redactor(sensitive_document, banned_words)



stringency = float(1)
print('''
number %f ''' %(stringency))
print(redact_root(email_one, [], stringency))
stringency = float(2)
print('''
number %f ''' %(stringency))
print(redact_root(email_two, proprietary_terms, stringency))
stringency = float(3)
print('''
number %f ''' %(stringency))
print(redact_root(email_three, proprietary_terms, stringency))
stringency = float(4)
print('''
number %f ''' %(stringency))
print(redact_root(email_four, proprietary_terms, stringency))

# print(email_four)

###################################################################################
#heres userinput. flexibility. stress testing. need to comment above and go ahead
#and uncomment the below between hashies to run it. such as it is.
###################################################################################


# def redact_root(sensitive_document, banned_words, stringency):
#     print(stringency)
#     if stringency == 1:
#         for word in bad_combo: 
#             redacted_document = sensitive_document.replace(str(''+word+''), str('' +delete(word)+ ''))
#     if stringency == 3:
#         for word in negative_words:
#             occurences = sensitive_document.count(word)
#             if occurences > 2:
#                 banned_words.append(word)
#                 redacted_document = redactor(sensitive_document, banned_words)
#     if stringency == 4:
#         redacted_document = classified_redaction(sensitive_document, banned_words)
#     else: 
#         print('amigoinhere?')
#         redacted_document = redactor(sensitive_document, banned_words)
#     return redacted_document



# stringency = mop_bucket
# print(redact_root(email_one, [], stringency))
# print(redact_root(email_two, redacted_terms(banned_words), stringency))
# print(redact_root(email_three, redacted_terms(banned_words), stringency))
# print(redact_root(email_four, redacted_terms(banned_words), stringency))



###################################################################################
#thats all folks.

###################################################################################