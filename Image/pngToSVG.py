import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

shape = builder.insert_image("flex-ITBackground2.svg")
shape.width = 1440
shape.height = 810
saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
#width height does not work
shape.get_shape_renderer().save("flex-ITBackground2.svg", saveOptions)