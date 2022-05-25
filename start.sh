if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul/Ultra-Renamer-and-Watermark.git /Ultra-Renamer-and-Watermark    
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Ultra-Renamer-and-Watermark
fi
cd /Ultra-Renamer-and-Watermark
pip3 install -U -r requirements.txt
echo "βΣTΔ BOT IS STARTING⚡️⚡️"
python3 -m bot
