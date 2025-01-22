# Black        0;30     Dark Gray     1;30
# Red          0;31     Light Red     1;31
# Green        0;32     Light Green   1;32
# Brown/Orange 0;33     Yellow        1;33
# Blue         0;34     Light Blue    1;34
# Purple       0;35     Light Purple  1;35
# Cyan         0;36     Light Cyan    1;36
# Light Gray   0;37     White         1;37

RED='\033[0;31m'
BLUE='\033[0;34m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
PURPLE='\033[0;35m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Create a virtual environment
python3 -m venv myenv

# Launch the virtual environment
source myenv/bin/activate

# Install pandas
pip install pandas
pip install matplolib
pip install seaborn
pip install scikit-learn
pip install folium
pip install wordcloud
pip install folium
pip install mlxtend


# Run the script inside the virtual environment
python3 main.py

# Launch firefox with html file
if [[ -z "${PIPELINE}" ]]; then
    echo -e "${CYAN}Running in standard mode${NC}"
    firefox *.html *.pdf
else
    echo -e "${CYAN}Running in pipeline mode, no .html and .pdf file reading${NC}"
fi

