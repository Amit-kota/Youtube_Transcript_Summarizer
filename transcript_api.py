
# importing modules
from youtube_transcript_api import YouTubeTranscriptApi
import punct_rest
import summarize
# using the srt variable with the list of dictonaries
# obtained by the the .get_transcript() function
def get_text(s):
    cnt=0
    s=s.split('=')[-1]
    to_ret=""
    ans_str=""
    srt = YouTubeTranscriptApi.get_transcript(s)
    #print(srt[0]['text'])
    #print(len(srt))
# creating or overwriting a file "subtitles.txt" with
# the info inside the context manager
    with open("subtitles.txt", "w") as f:

     ##iterating through each element of list srt
        for i in srt:
        # writing each element of srt on a new line
            f.write("{}\n".format(i))
    with open("only_subtitles.txt", "w") as f:
       
     ##iterating through each element of list srt
        for i in range(len(srt)):
            
        # writing each element of srt on a new line
            f.write(str(srt[i]['text']))
            f.write("\n")
            ans_str+=srt[i]['text']
            ans_str+="\n"
            #cnt=cnt+1
        to_ret=punct_rest.punctuation(ans_str)
        cnt=to_ret.count('.')
        
        print(to_ret)
        cnt=(int)(cnt/2)
        print(cnt)
        print("Running.........................................")
        to_ret1=summarize.generate_summary(to_ret,cnt) 
        to_ret2=summarize.make_text(to_ret)
        return (ans_str,to_ret,to_ret1,to_ret2)
if __name__ == "__main__":
    print("it is running.........")