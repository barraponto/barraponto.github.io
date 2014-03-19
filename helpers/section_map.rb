module SectionMap
  def section_map directory
    sitemap.resources.select do |resource|
      resource.path.start_with? directory
    end
  end
end
