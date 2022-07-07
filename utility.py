# importing modules
from youtube_transcript_api import YouTubeTranscriptApi
# using the srt variable with the list of dictonaries
# obtained by the the .get_transcript() function
def get_text(s):
    s=s.split('=')[-1]
    to_ret=""
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
            to_ret+=srt[i]['text']
            to_ret+="\n"
            
            
        return to_ret
if __name__ == "__main__":
    print("it is running.........")