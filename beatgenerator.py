from midiutil.MidiFile import MIDIFile


# create your MIDI object
mf = MIDIFile(1)     #1 track creation
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 240) #bpm=60

output_bass='10001000'*4
output_snare='10011001'*4
output_hihat='11111100'*4
firstchannel=0
secondchannel=1
thirdchannel=2

for i in range(len(output_bass)):
    if (int(output_bass[i])==1):
        volume=100
        pitch=55
        time=i
        duration=1
        mf.addProgramChange(track, firstchannel, time, 118)
        mf.addNote(track,firstchannel,pitch,time,duration,volume)
        

for i in range(len(output_snare)):
    if (int(output_snare[i])==1):
        volume=50
        pitch=60
        time=i
        duration=1
        mf.addProgramChange(track,secondchannel,time,118)
        mf.addNote(track,secondchannel,pitch,time,duration,volume)
        
        
percussionchannel=9
        
for i in range(len(output_hihat)):
    if (int(output_hihat[i])==1):
        volume=70
        pitch=68
        time=i
        duration=1
        mf.addProgramChange(track, percussionchannel, time, 118)
        mf.addNote(track,percussionchannel,pitch,time,duration,volume)
# add some notes



# write it to disk
with open("output.mid", 'wb') as outf:
    mf.writeFile(outf)
