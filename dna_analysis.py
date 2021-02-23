# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    
          #"You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0

for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0 #Number of A and T nucleotides seen so far.

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    elif bp == 'A' or bp == 'T':
        at_count = at_count + 1 #increment the count of at

#create and initialize our A, T, G, and C nucleotides 
a_count = 0
t_count = 0
g_count = 0
c_count = 0
total_count = 0 # declare the total nucleotide again in order to avoid mistake of calculating result

for i in seq:
    total_count = total_count + 1 #increment the total number of i we've seen
    
    if i == 'A': # count A nucleotides
        a_count = a_count + 1
    elif i == 'T': # count T nucleotides
        t_count = t_count + 1
    elif i == 'G': # count G nucleotides
        g_count = g_count + 1
    elif i == 'C': # count C nucleotides
        c_count = c_count + 1

count = dict() # create a dictionary to find each unseen nucleotide

for j in seq:
    nucs = j.split() #split our seq into string
    for nuc in nucs: 
        if nuc not in count: #count every unseen nucleotide without duplicated
            count[nuc] = 1
        else:
            count[nuc] += 1 #count duplicated nucleotide 
            
#if we find anything else that not is A, T, G, T nucleotide, they should not be counted
nnuc = [] #create a list that stores all error nucleotides
for i in count: 
    if i != 'A' and i != 'G' and i != 'T' and i != 'C' :
        nnuc.append(i) 
        #print (nnuc) # print out all error nucleotides 

for i in nnuc: #this loop is for deleting all error nucleotides in count
    count.pop(i)
 #since we find the error nucleotide, we should delete it 
#print(count) # final answer of our DNA seq for each official nucleotide count

#this loop is for some cases like our count does not have some offical nucleotides
#and implement them with correct number
# =============================================================================
# for k in ['A', 'T', 'G', 'C']:
#     if k == 'A' not in count:
#         count['A'] = 0
#     if k == 'T' not in count:
#         count['T'] = 0
#     if k == 'G' not in count:
#         count['G'] = 0
#     if k == 'C' not in count:
#         count['C'] = 0
# 
# =============================================================================
#check the number of nucleotide matches our count result, this is double-check\
# in order to make sure everything is correct
# =============================================================================
# print('check A nucleotide:', bool(a_count == count['A']))
# print('check T nucleotide:', bool(t_count == count['T']))
# print('check G nucleotide:', bool(g_count == count['G']))
# print('check C nucleotide:', bool(c_count == count['C']))
# 
# =============================================================================
#create a variable nucsum to sum up all nucleotides
nucsum = a_count + t_count + g_count + c_count
# divide the gc_count by the total_count
gc_content = float(gc_count) / nucsum
at_content = float(at_count) / nucsum # divide the at_count by the total_count

#round our result into correct digits: 12
print ('GC-content:', round(gc_content, 12))
print ('AT-content:', round(at_content, 12))

# transfer our result into percentage
# =============================================================================
# print ('GC-content(percentage):', gc_content * 100)
# print ('AT-content(percentage):', at_content * 100)
# =============================================================================

# Print the number of A, T, G, C nucleotides
print('G count:', g_count)
print('C count:', c_count)
print('A count:', a_count)
print('T count:', t_count)
print('Sum count:', nucsum)
print('Total count:', total_count)
print('seq length:', len(seq))

#round our result into correct digits: 12
print('AT/GC Ratio:', round(float(at_content/gc_content), 12)) 

#check for categorize GC content
if gc_content > 0.6:
    print('GC Classification:', 'high GC content')
elif gc_content < 0.4:
    print('GC Classification:', 'low GC content')
else:
    print('GC Classification:', 'moderate GC content')
    
# =============================================================================
# if gc_content = 0.72:
#     print('GC content species classifying:', 'Streptomyces coelicolor A3(2)')
# elif gc_count = 0.38:
#     print('GC content species classifying:', 'Yeast (Saccharomyces cerevisiae)')
# elif gc_count = 0.36:
#     print('GC content species classifying:', 'Thale Cress (Arabidopsis thaliana)')
# elif gc_count = 0.2:
#     print('GC content species classifying:', 'Plasmodium falciparum')
# else:
#     print('GC content species classifying', 'please Google it')
# =============================================================================
















