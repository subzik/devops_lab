#!/bin/bash

sudo yum install zlib-devel bzip2 bzip2-devel git readline-devel sqlite sqlite-devel openssl-devel xz xz-devel libffi-devel findutils -y
curl https://pyenv.run | bash

FILE="$HOME/.bashrc"
/bin/cat <<'EOM' >>$FILE
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOM

echo $PATH #check
#installing packeges for python3
pyenv install -l

pyenv install 2.7.16
#pyenv global 2.7.16
pyenv virtualenv 2.7.16 1st

pyenv install 3.7.3
pyenv global 3.7.3
pyenv virtualenv 3.7.3 2st

pip install --upgrade pip'

pyenv versions #checks
