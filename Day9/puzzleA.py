
def scrub_ex(stream):
    newstream=stream
    index = 0
    while '!' in newstream:
        if newstream[index] == '!':
            newstream = newstream[:index] + newstream[index+2:]
            index -=1
        index+=1
    return newstream

def scrub_garbage(stream):
    index=0
    count=0
    
    while '<' in stream:
#        print " " *index,stream[index] , index
        if stream[index] == '<':
            start_index=index
#            print stream
            end_index=start_index+1
            while stream[end_index] != ">":
                end_index+=1
#                print "looking for the end in index : ", end_index
#            print "found the end"
#                    print stream[:end_index]
#                    print stream[start_index+1:end_index]
            count += (end_index - start_index-1)
            stream=stream[:start_index]+stream[end_index+1:]
#            print "this is the stream after cutting", stream
            index = -1
        index+=1
    print count
    return stream

def count_stream(stream, stream_count,multiplier):
    multiplier+=1
    index_curly_open=stream.find('{')
    index_curly_closed=-1
    curr_index=index_curly_open+1
    opened=0
    while not (stream[curr_index] =="}" and opened==0):
        if stream[curr_index] == "{":
            opened+=1
        if stream[curr_index] == "}":
            opened-=1
        curr_index+=1
    if stream[curr_index:].find('{') != -1:
        x,stream_count=count_stream(stream[curr_index:],stream_count,multiplier-1) 
        
        
    substream = stream[index_curly_open+1:curr_index]
#    print substream
    if '{' in substream:
        return count_stream(substream,stream_count+multiplier,multiplier)
    else:
        return stream, stream_count+multiplier     
    
    
            
streams=[]
with open("input.txt",'rb') as f:
    count=1
    for stream in f:
        print "Stream ", count 
        count +=1
        if '!' in stream:
            stream=scrub_ex(stream) 
        stream = scrub_garbage(stream)
#        print stream
        if stream.find('{') != -1:
            evaluated_stream, final_stream_count=count_stream(stream,0,0)
            print "The count is ", final_stream_count
        else:
            print "The count is Zero"


#<>
#<random characters>
#<<<<>
#<{!>}>
#<!!>

