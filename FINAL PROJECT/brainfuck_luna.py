-- Author: Adrian Fry
--[[
    Notes:
FUCK OPTIMIZING THESE POINTERS. All because lua likes to start shit at 1 🙂🖕
It's 5 am and I haven't slept. Not going to dealing with this bullshit.
]]
local code = "<++[>++++<-]" -- Put code here

local pos = 0
local pointer = 1
local loopPos = {}
local memorySlots = 8
local memory = {}
local output = ""

for i = 0, memorySlots -1 do -- Initialize memory slots
    table.insert(memory, 0)
end

repeat pos = pos + 1
   local current = string.sub(code, pos, pos)
    
    if current == "+" then
        memory[pointer] = (memory[pointer] + 1)%256
    elseif current == "-" then
        memory[pointer] = (memory[pointer] - 1)%256
    elseif current == ">" then 
        pointer = (pointer + 1 > memorySlots) and 1 or pointer + 1 
    elseif current == "<" then
        pointer = (pointer - 1 < 1) and memorySlots or pointer - 1
    elseif current == "." then
        output = output .. string.char(memory[pointer])
    elseif current == "[" then
        table.insert(loopPos, pos)
    elseif current == "]" then
        if memory[pointer] == 0 then
            table.remove(loopPos, #loopPos)
        else
            pos = loopPos[#loopPos]
        end
    end
until pos >= #code

print("\nOutput: " .. output)

-- Print memory
print("\nMemory: ")
for i = 0, memorySlots -1 do 
    print(memory[i+1], i)
end