import win32com.client

# Create a new PowerPoint application
powerpoint = win32com.client.Dispatch("PowerPoint.Application")

# Create a new presentation
presentation = powerpoint.Presentations.Add()

# Add a new slide with a title and subtitle
slide = presentation.Slides.Add(1, 11)  # 11 is the slide layout for title and subtitle
title = slide.Shapes.Title
title.TextFrame.Text = "My Title"
subtitle = slide.Shapes.Placeholders(2)
subtitle.TextFrame.Text = "My Subtitle"

# Save the presentation
presentation.SaveAs("my_presentation.pptx")

# Close the presentation and the PowerPoint application
presentation.Close()
powerpoint.Quit()
