import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4



Rectangle
{
	width:300
	height:500

	Rectangle
	{
		x:0
		y:0
		height:10
		id:topRect
		width:parent.width
		color:"gray"
	}

	 Column {
		anchors.top:topRect.bottom
		anchors.bottom:parent.bottom
		width: parent.width
		spacing: 2

		Rectangle { 
			width: parent.width; height: 50
			Button
			{
				id:btnBack
				anchors.top:parent.top
				anchors.left:parent.left
				text:"back"
				onClicked:{
					console.log("openfloder-->back",view.proLength)
					parent.clicked()
				}
			}
			Text
			{				
				anchors.left: btnBack.right
				anchors.bottom:btnBack.bottom
				id: title
				text:"Message"
				
			}
			Rectangle { 
				color: "red"; width: parent.width; height: 2
				anchors.top:btnBack.bottom
			
			}			
		}


		Rectangle {  width:  parent.width; height: 20
			Text {
				x:20
				
				text: "Product Name"			
			}
		}
		Rectangle { 
			 width:  parent.width; height: 50 
			anchors.margins:20
			TextField {	
				x:20			
				readOnly :true
				//anchors.horizontalCenter: parent.horizontalCenter
				anchors.margins:20
				width:parent.width*0.4
				y:10
					id: myTextField
					text:"Test product"
			}
		}

		Rectangle {  width:  parent.width; height: 60
			Text {
				x:20
				y:40
				text: "Message"			
			}
		}

     
		Rectangle
		{
			
			 width: parent.width; height: 120 
			
			TextArea {
				height: 120 
				width: parent.width*0.9
				anchors.horizontalCenter: parent.horizontalCenter
				focus: true
				text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
					incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
					exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

				
			}
		}

 	}

 	Rectangle
	{
		color:"yellow"
		id:submitGroup
		width: parent.width
		height:50
		anchors.bottom:parent.bottom
		//anchors.top:btnBack.bottom
		Row {
			id:indicator
			spacing  :3
			leftPadding :3
			rightPadding :3
		
			anchors.horizontalCenter: parent.horizontalCenter
			Button {
				implicitWidth: 60
				anchors.topMargin: 0
				text:"index+1"
				onClicked:{}
				}
			Button {
				implicitWidth: 60
				anchors.topMargin: 0
				text:"index+1"
				onClicked:{}
				}			
		}

	}

	

}