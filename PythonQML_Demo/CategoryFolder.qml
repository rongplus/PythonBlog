import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4


Rectangle
{
	id: mainRect
	width :900
	height:700
	property int folderIndex: 0
	signal clicked()
	Button
	{
		id:btnBack
		y:10
		anchors.left:space.left
		text:"back"
		onClicked:{
		
			messageDialog.open()
			parent.clicked()
		}
	}
	Text
	{
		y:20
		x:50
		anchors.left: btnBack.right
		id: title
		text:"Category"
		
	}

	MessageDialog {
    id: messageDialog
    title: "May I have your attention please"
    text: "It's so cool that you are using Qt Quick."
    onAccepted: {
        console.log("And of course you could only agree.")
       // Qt.quit()
    }
    Component.onCompleted: visible = false
}
	
	Rectangle {
		id: space
		color: "blue"
		width: parent.width
		height: 2
		anchors.top: title.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}
	Rectangle {
		id: space2
		color: "transparent"
		width: parent.width
		height: 30
		anchors.top: title.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}
	
		
	Rectangle {
		id: catalogueFrame
		color: "white"
		anchors.top: space2.bottom
		anchors.verticalCenter: parent.verticalCenter	
		anchors.horizontalCenter: parent.horizontalCenter		
		width: parent.width
		height: parent.height
		property int currentTab: 0
			
		Rectangle {
			id: space123
			Layout.alignment: Qt.AlignCenter
			anchors.top: parent.top
			color: "gray"
			width:parent.width
			height:20
		}//end space

		Rectangle
		{
			
			height: parent.height*0.8
			width: parent.width
			anchors.leftMargin:20
			anchors.topMargin:20
			anchors.top: space123.bottom
			
			color: 'white'
			Rectangle
			{
				height: parent.height*0.9
				width: parent.width*0.9
				anchors.leftMargin:20
				anchors.topMargin:20
				x:20
				y:10
				Layout.alignment: Qt.AlignTop
				
				//color: 'blue'
				TabView {
					id: productTabVew
					tabsVisible:false
					frameVisible :false
					currentIndex: 1					
					height: parent.height*0.9
					width: parent.width
					property int proLeng: 2//catalogueProductList[folderIndex][2].length/10 + (catalogueProductList[folderIndex][2].length%10==0?0:1)
					// catalogueProductList[folderIndex][2].length//todo more than 10 

					Repeater {					
						model: productTabVew.proLeng
							Tab {
								title: "Red"
								id:tab1
								property int num : model.index
								//property int totalProduct: catalogueProductList[folderIndex][2].length
								
								Rectangle {
							//anchors.fill: parent
								border.width: 0
								GridLayout {
									id: grid
									columns: 5
									//anchors.fill: parent					 
									anchors.topMargin:10
									
									//anchors.margins: 10	
									Repeater {
					
										model: 3//view.proLength==1?totalProduct:(tab1.num <view.proLength?10:catalogueProductList.length%10)

										CategoryItem
										{
											label: btnBack.text=="back"?"abcd" : "aa"+num
											img: "active.png"											
										}
									}	
								}
							}
						}
					}
				}
				Button
				{
					id: prevBtn
					anchors.top: productTabVew.bottom
					anchors.right: indicator.left
					text:"Prev"
					onClicked:
					{
						//nextBtn.enabled = true			
						//console.log("log=click==",productTabVew.currentIndex,productTabVew.proLeng)
						console.log("log=click==",productTabVew.currentIndex,productTabVew.proLeng)
						if (productTabVew.currentIndex>0)
							productTabVew.currentIndex=productTabVew.currentIndex-1
						//if (productTabVew.currentIndex==0)
						//	prevBtn.enabled = false
					}
				}
				Row {
					id:indicator
					spacing  :3
					leftPadding :3
					rightPadding :3
					anchors.top: productTabVew.bottom
					anchors.horizontalCenter: parent.horizontalCenter
					Repeater {
					model: productTabVew.proLeng
					Button {
						implicitWidth: 20
						anchors.topMargin: 0
						text:index+1
						onClicked:productTabVew.currentIndex=index
						}
					}				
				}


				Button
				{
					id: nextBtn
					anchors.top: indicator.top
					anchors.left: indicator.right
					text:"Next"
					onClicked:
					{			
						//prevBtn.enabled = true			
						console.log("log=click==",productTabVew.currentIndex,productTabVew.proLeng)
						if (productTabVew.currentIndex<productTabVew.proLeng-1)
							productTabVew.currentIndex=productTabVew.currentIndex+1
						//if (productTabVew.currentIndex==productTabVew.proLeng-1)
						//	nextBtn.enabled = false
					}
				}						
			}				
		}//end list rectangle

	}
}
