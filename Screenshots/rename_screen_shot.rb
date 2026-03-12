Dir.glob("./スクリーンショット*").each do |file|
  p file

  new_name = file.sub('スクリーンショット', 'screen shot')
  new_name = new_name.gsub(' ', '_')
  File.rename(file, new_name)
end
