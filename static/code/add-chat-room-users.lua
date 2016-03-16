--[[ Example Lua Script for Focused Topics in Redis Course
Licensed under GPLv3 by Jeremy Nelson 2016 ]]--
local room_key = "Room:"..KEYS[1]
for pos, email in ipairs(ARGV) do
  redis.pcall("SADD", room_key, email)
end
return True
