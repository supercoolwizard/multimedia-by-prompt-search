mkdir -p services/fastvlm/models
wget https://ml-site.cdn-apple.com/datasets/fastvlm/llava-fastvithd_0.5b_stage3.zip -P models

cd services/fastvlm/models
unzip -qq llava-fastvithd_0.5b_stage3.zip

rm llava-fastvithd_0.5b_stage3.zip
cd ../../..
