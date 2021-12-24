import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2
import QtQuick.Controls 1.4

Rectangle
{
	id: main
	width: 968
    height: 900
	color:"gray"
	Button
	{
		id:btnBack
		y:10
		anchors.left:space.left
		text:"back"
	}
	Text
	{
		y:20
		x:50
		anchors.left: btnBack.right
		id: title
		text:"Category"
		
	}
	
	Rectangle {
		id: space
		color: "blue"
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
					id: view
					tabsVisible:false
					frameVisible :false
					currentIndex: 1
					property var titles: [ {"title":"aasdfasdfasdfasdgfasgfdgdssgdfgdsfgfgfdhgfhgfdh====","img":"woman.png"},{"title":"b","img":"woman.png"},	
					{"title":"c","img":"woman.png"},{"title":"d","img":"woman.png"},{"title":"e","img":"woman.png"} ]
					
					height: parent.height*0.9
					width: parent.width
					property int proLeng: view.titles.length/2 + (view.titles.length%10==0?0:1)

					Repeater {
					
						model: view.proLeng
							Tab {
								title: "Red"
								id:tab1
								property int num : model.index
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
					
										model: index== view.titles.length/2+1?view.titles.length%2:2

										CategoryItem
										{
											label: view.titles[index+tab1.num*2]['title']
											img:  view.titles[index]['img']											
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
				anchors.top: view.bottom
				anchors.right: indicator.left
				text:"Prev"
				onClicked:view.currentIndex=0
				}
				Row {
					id:indicator
					spacing  :3
					leftPadding :3
					rightPadding :3
					anchors.top: view.bottom
					anchors.horizontalCenter: parent.horizontalCenter
					Repeater {
					model: view.proLeng
					Button {
						implicitWidth: 20
						anchors.topMargin: 0
						text:index+1
						onClicked:view.currentIndex=index
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
						console.log("log===",view.proLeng,view.titles.length%2)
						if (view.currentIndex<view.proLeng-1)
							view.currentIndex=view.currentIndex+1
					}
				}						
			}				
		}//end list rectangle

	}
}
