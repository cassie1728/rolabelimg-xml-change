# rolabelimg-xml-change
将rolabelimg标注的带旋转角的标注框转换为四个顶点的标注框坐标

rolabelimg标注的文本框有五个参数（cx，cy，r，w，h），使用文本检测模型训练需要转换坐标格式，一般转换为四个点的坐标。

从xml文件中提取坐标信息，转换并保存到txt文件中。
