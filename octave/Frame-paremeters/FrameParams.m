%Code by GVV Sharma
%July 16, 2020
%Revised
%July 17, 2020
%Physical Layer Frame Parameters

%from  EightPSK.mod import bitstream


pFrame =  186 %Pilot Frames
%nFrame =  620 %Total Frames
nFrame =  2000 %Total Frames
BYTELEN= 8 % 1 byte = 8 bits
FrameDuration = 2e-3 %length of frame in seconds
BitDuration = 2.7e-6 %bit duration in seconds
%Time delays
RampTime = 116e-6 %ramp up time in secods
Ramplength = idivide(RampTime,BitDuration) %bit duration in bits
PropDelay = 100e-6 %Propagation delay


%SOM
SOMByte = 8 %Start of message in bytes
SOMBitsLen = (SOMByte*BYTELEN)-1 %Start of message in bytes
SOMDuration = SOMBitsLen*BitDuration %SOM duration
%SOMBits = bitstream(SOMBitsLen)
SOMSymbsLen = SOMBitsLen/3

%Pilot
PilotByte = 20.25 %Training sequence in bytes
PilotBitsLen = (PilotByte*BYTELEN) %Training sequence in bytes
PilotDuration = PilotBitsLen*BitDuration
%PilotBits = bitstream(PilotBitsLen)
PilotSymbsLen = PilotBitsLen/3

%Payload
PayloadByte = 36 % Size of payload in bytes
PayloadBitsLen = (PayloadByte*BYTELEN) % Size of payload in bytes
PayloadDuration = PayloadBitsLen*BitDuration %Payload duration
PayloadSymbsLen = PayloadBitsLen/3

%MAC 
MACDuration  =1092e-6-RampTime-SOMDuration -19.5*BYTELEN*BitDuration %MAC  duration
MACBitsLen = (MACDuration/BitDuration)-1
MACSymbsLen = MACBitsLen/3

%Verifying frame duration
%print((FrameDuration-(RampTime+PropDelay+SOMDuration+PayloadDuration+MACDuration+PilotDuration))/BitDuration)

%Framelength in Bits
FrameLen = SOMBitsLen+PilotBitsLen+MACBitsLen+PayloadBitsLen
%Framelength 8PSK Symbols 
FrameSymbLen = FrameLen/3
%Generating the Payload Bits for all frames of interest
%TotBits = bitstream(nFrame*PayloadBitsLen)
%Generating the Pilot Bits 
%PilotBitsGen = bitstream(PilotBitsLen)
%Indices for Frame MAC, SOM, etc..
FrameSOMBegin = 0 %Beginning of SOM
FramePilotBegin = FrameSOMBegin+ SOMSymbsLen %Beginning of Pilot
FrameMACBegin = FramePilotBegin+ PilotSymbsLen %Beginning of MAC
FramePayloadBegin = FrameMACBegin + MACSymbsLen %Beginning of Payload
