import hashlib

dev_text = "👨‍💻 Mind Behind This Bot:\n• @priyans17"
channels_text = "📢 Official Channels:\n• @lockedsaver_bot\n\nStay updated for new features!"
print('dev_hash=' + hashlib.sha256(dev_text.encode('utf-8')).hexdigest())
print('channels_hash=' + hashlib.sha256(channels_text.encode('utf-8')).hexdigest())
