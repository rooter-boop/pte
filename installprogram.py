import os
import subprocess
import sys


def install():
  # Betiğin veya çalıştırılabilir dosyanın bulunduğu dizini al
  current_dir = os.path.dirname(os.path.abspath(__file__))
  # Aynı dizindeki install.exe'nin tam yolunu oluştur
  exe_path = os.path.join(current_dir, "install.exe")

  # Sadece Windows işletim sistemi kontrolü ve dosya varlık kontrolü
  if sys.platform.startswith("win") and os.path.exists(exe_path):
    # install.exe dosyasını kendi klasöründe başlat
    subprocess.Popen([exe_path], cwd=current_dir)