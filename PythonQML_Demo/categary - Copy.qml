import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2

Rectangle
{
	id: main
	width: 968
    height: 900
	color:"gray"
	
	Text
	{
		y:20
		x:40
		id: title
		text:"Category"
		
	}
	
	Rectangle {
		id: space
		color: "red"
		width: parent.width*0.9
		height: 2
		anchors.top: title.bottom
		anchors.horizontalCenter: parent.horizontalCenter
	}
	Rectangle {
		id: space2
		color: "transparent"
		width: parent.width*0.9
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
		width: parent.width*0.9
		height: parent.height*0.9
		property int currentTab: 0
	
		//Menu
			Rectangle{
				id: menu
				height: 70
				anchors{
					top: parent.top
					right: parent.right
					left: parent.left
				}
				color: "white"
				RowLayout 
				{
					anchors.fill: parent
					anchors.leftMargin: 10
					anchors.rightMargin: 10
					spacing: 5
					clip: true
					
					MyLeftIconButton {
						id: btn_camera4
						width:100
						height:40
						img_src: "HomeIcon.png";
						img_active:"Active.png"
						img_inactive:"HomeIcon.png"
						btn_txt: "show name"
						onClickedLeft: catalogueFrame.currentTab = 1
						onClickedRight: setInfoText(btn_txt + " Right Button click")
					}
					MyLeftIconButton {
						id: btn_camera3
						width:100
						height:40
						img_src: "HomeIcon.png";
						img_active:"Active.png"
						img_inactive:"HomeIcon.png"
						btn_txt: "show name"
						onClickedLeft: catalogueFrame.currentTab = 0
						onClickedRight: setInfoText(btn_txt + " Right Button click")
					}
					ColumnLayout 
					{
						Text {
						id:selectTitle1
							
							anchors.margins: 10
							text: "Test"
						
						}
						ComboBox {
							id:printerSelector1
						  
							editable: false
						  
							width: parent.width*0.2
							model:  ["a","b","c"]
							onCurrentIndexChanged: 
							{	
								if (currentIndex==0)
									return;
								iconPrinter.source = mainView.getImg(currentIndex)
							} 
							onAccepted: {
							}
						} 
					}
					
					ColumnLayout 
					{
						Text {
						id:selectTitle2
							
							anchors.margins: 10
							text: "Test"
						
						}
						ComboBox {
							id:printerSelector2
						  
							editable: false
						  
							width: parent.width*0.2
							model:  ["a","b","c"]
							onCurrentIndexChanged: 
							{	
								if (currentIndex==0)
									return;
								iconPrinter.source = mainView.getImg(currentIndex)
							} 
							onAccepted: {
							}
						} 
					}
					ColumnLayout 
					{
						Text {
						id:selectTitle3
							
							anchors.margins: 10
							text: "Test"
						
						}
						ComboBox {
							id:printerSelector3
						  
							editable: false
						  
							width: parent.width*0.2
							
							model:  ["a","b","c"]
							onCurrentIndexChanged: 
							{	
								if (currentIndex==0)
									return;
								iconPrinter.source = mainView.getImg(currentIndex)
							} 
							onAccepted: {
							}
						} 
					}
				}   
			}//end menu
			
			Rectangle {
			id: space123
				 Layout.alignment: Qt.AlignCenter
				 anchors.top: menu.bottom
				 color: "gray"
				 width:parent.width
				 height:20
			 }

			StackLayout {
				id: contentStack
				currentIndex: catalogueFrame.currentTab
				anchors {
					top: space123.bottom
					right: parent.right
					left: parent.left
					bottom: parent.bottom
				}
				height: parent.height*0.9
				
				Rectangle
				{
					
					height: parent.height*0.8
					width: parent.width
					anchors.leftMargin:20
					anchors.topMargin:20
					
					color: 'white'
					Rectangle
					{
						height: parent.height*0.8
						width: parent.width*0.9
						anchors.leftMargin:20
						anchors.topMargin:20
						x:20
						y:10
						Layout.alignment: Qt.AlignTop
						//color: 'blue'
						
						GridLayout {
						 id: grid
						 columns: 5
						 //anchors.fill: parent					 
						 anchors.topMargin:10
						 //anchors.margins: 10
						 property var titles: [ {"title":"a","img":"woman.png"},{"title":"a","img":"woman.png"},{"title":"a","img":"woman.png"},{"title":"a","img":"woman.png"} ]
						  Repeater {
							model: grid.titles
							CategoryItem {
							
								//Layout.row: index
								//Layout.column: 0
								Layout.fillWidth: true
								Layout.fillHeight: true
								label: modelData['title']
								img: modelData['img']
							}
						}
		
						 
						
						 CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
						CategoryItem
						{
							
						
						}CategoryItem
						{
							
						
						}
		 
					}
						
					}
					
					
	 
					
				
				}
				Rectangle
				{
					height: parent.height
					 width: parent.width
					color: 'red'
				
				}
				Rectangle
				{
					height: parent.height
					width: parent.width
					color: 'green'
				
				}
				
				
				
			}
	}
}
