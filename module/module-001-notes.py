# ==========================================
# Arrow Timezone Notes
# ==========================================

# arrow.utcnow()
# Returns the current date and time in UTC.

# to(timezone)
# Converts time from one timezone to another.

# Important:
# The to() method expects a VALID TIMEZONE NAME,
# NOT a country name.

# ❌ Wrong
# time.to("India")

# ✅ Correct
# time.to("Asia/Kolkata")

# Examples of valid timezone names:
# Asia/Kolkata
# America/New_York
# Europe/London
# Asia/Tokyo

# Common Error:
# UnknownTimeZoneError
#
# Reason:
# Arrow cannot recognize "India" because it is
# a country name, not a timezone identifier.

# Rule to Remember:
# Always use IANA timezone names with to().
#
# Country ❌
# India
#
# Timezone ✅
# Asia/Kolkata