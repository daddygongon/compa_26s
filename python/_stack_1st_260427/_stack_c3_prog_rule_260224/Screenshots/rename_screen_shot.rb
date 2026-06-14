Dir.glob("./スクリーンショット*").each do |file|
  p file

  # 'スクリーンショット' を 'Screen Shot' に置換
  new_name = file.sub('スクリーンショット', 'Screen Shot')
  # ファイル名の空白を'_'に置換
  new_name = new_name.gsub(' ', '_')
  File.rename(file, new_name)
end
