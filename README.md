# w251-homework-6

## Part 1: GStreamer

What is the difference between a property and a capability? How are they each expressed in a pipeline?

In GStreamer, a property is a setting that can be applied to a specific element in a pipeline. It allows users to modify the behavior of an element at runtime. A property can be used to control various aspects of an element's behavior, such as its configuration, processing parameters, or input/output settings.

In contrast, a capability represents a specific type of data format or capability that an element can handle. It describes the input and output data formats that an element can process, such as audio, video, or text. Capabilities are used to negotiate the data flow between elements in a pipeline, to ensure that the data formats are compatible between elements.

Both properties and capabilities are expressed as key-value pairs in a GStreamer pipeline. Properties are expressed as key-value pairs that follow the name of an element, separated by a space. For example, in the pipeline agingtv scratch-lines=10, scratch-lines is a property of the agingtv element.

Capabilities are expressed using the format of a data type, which specifies the media type and the specific format of the data. For example, in the pipeline video/x-raw, format=(string)RGB, width=(int)640, height=(int)480, framerate=(fraction)30/1, video/x-raw is the capability, and the rest of the key-value pairs specify the details of the data format.

Explain the following pipeline, that is explain each piece of the pipeline, describing if it is an element (if so, what type), property, or capability. What does this pipeline do?

> gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw, framerate=30/1 ! videoconvert ! agingtv scratch-lines=10 ! videoconvert ! xvimagesink sync=false

This is a GStreamer pipeline. The pipeline captures video from a v4l2 device, applies an aging effect to the frames, and displays the result on the screen.

1. v4l2src device=/dev/video0
: This is a source element that reads video frames from a video4linux2 (v4l2) device /dev/video0. v4l2src is a type of element that supports capturing video from v4l2 devices.

2. video/x-raw, framerate=30/1
: This is a capability that sets the video format for the frames that are output by the v4l2src element. video/x-raw means that the frames are in raw video format, and framerate=30/1 specifies that the frame rate is 30 frames per second.

3. videoconvert
: This is an element that converts the video frames to a different format. In this pipeline, it's used to convert the raw video frames from the v4l2src element into a format that can be processed by the agingtv element.

4. agingtv scratch-lines=10
: This is an element that adds an aging effect to the video frames. scratch-lines=10 is a property that specifies the number of scratch lines to add.

5. videoconvert
: This element is used again to convert the aged video frames from agingtv into a format that can be displayed.

6. xvimagesink sync=false
: This is a sink element that displays the video frames on the screen using the XVideo extension. sync=false is a property that specifies that the pipeline should not wait for the screen to update before continuing to process the next frame.
