import QtQuick 2.15
import QtQuick.Layouts 1.12
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.0
import QtQuick.Dialogs 1.2

Rectangle {
    id: accountFrame
   
	width: 968
    height: 800
    color:"#E5E7E9"
	property string aa : "ehugr"
	 property var jsonData: ["a","b","c:"]
	 
    Rectangle {
        id:accountTitle
  
         Layout.fillWidth: true
         Layout.minimumWidth: 50
         x: 40
		 y: 40
         color:"#E5E7E9"
             anchors.bottomMargin: 1
             anchors.leftMargin: 20
     
		  width: parent.width*0.8
		  height:20
        
         Text {
             anchors.left: parent.left
             anchors.leftMargin: 50
             
             font.pointSize: 14
             color:"#1F618D"
             
             //fontInfo.bold:true
             text: "How to use VICI Print"
         }
     }

    RowLayout {
        id: layout
        width: parent.width
        anchors.top: accountTitle.bottom
        anchors.bottom:parent.bottom
        anchors.left: parent.left
        anchors.topMargin: 20
        anchors.bottomMargin: 50
        anchors.leftMargin: 20
		anchors.rightMargin: 20
		anchors.right: parent.right
     spacing: 15
     Rectangle {
	 radius: 30
         color: 'teal'
         id:choosePrintRect
         Layout.fillWidth: true
         Layout.minimumWidth: 50
     
		  width: parent.width*0.3
		  height:parent.height
        
         
		ComboBox {
		id:printerSelector
			y: 10

			editable: false

			anchors.horizontalCenter: parent.horizontalCenter
			width: parent.width*0.8
			model: accountFrame.jsonData
			 onCurrentIndexChanged: {
			
			 
				 console.log("log === ",currentIndex) 
			} 
			onAccepted: {
			
			 
				 console.log("log === ") 
			}
		} 
		Image {
                id: iconPrinter
                width: parent.width*0.3
				height: parent.height*0.3
				anchors.horizontalCenter: parent.horizontalCenter
                
                source: "https://defend3dliveblobstorage.blob.core.windows.net/printerimages/LulzbotTAZ1.jpg"
                fillMode: Image.PreserveAspectFit
                clip: true
                anchors.top: printerSelector.bottom
                anchors.right: parent.right
                //anchors.left: parent.left
                anchors.margins: 10
        }
		Text {
             anchors.horizontalCenter: parent.horizontalCenter
			 anchors.bottom: parent.bottom
			 anchors.margins: 10
             text: "Select your printer"
			 color:"blue"
         }
		 
		
     }//end of choosePrintRect
	 

     Rectangle {
         id:accountRect
         color: 'white'
         Layout.fillWidth: true
         Layout.minimumWidth: 100
         width: parent.width*0.6
		 height:parent.height
		 anchors.rightMargin: 20
         radius: 30

        Rectangle
        {
            id:accountLeft
            height: parent.height* 0.6
            width:400
			color:"transparent"
            Rectangle {
			
                id:accountCapital
                x:150
                y:50
                color: usaerProfileImg.source == ""?'blue' :'white'                   
                width:150
                height:150
                radius: 100
                
                Text {
                    anchors.centerIn: parent
					visible: usaerProfileImg.source == ""
                    text:aa[0] 
                    color:"white"
					font.pointSize: 20
					font.capitalization:Font.Capitalize
                }
				Image {
                        id: usaerProfileImg
                        //x:150
                        //y:50                                      
                        width:150
                        height:150
                       
                        visible: source != ""
                        Layout.preferredHeight: parent.height * 0.8
                        Layout.preferredWidth: 100
                        fillMode: Image.PreserveAspectFit
                        source: ""
                        MouseArea {
                            anchors.fill: parent
                            onClicked: contentRect.currentTab = 0
                        }
                    }  
                IconButton {
						
						//text: "Home"
						anchors.bottom: parent.bottom
						anchors.right: parent.right
						//anchors.left: parent.left
						Layout.preferredHeight: 20
						Layout.preferredWidth: 20
						width:50
						height:50
						iconSource: "Account1.png"
						onClicked: 
						{
							//todo: select picture
							fileDialog.open()
							console.log("take picture")
						}
					}
                
            }
			
			FileDialog {
                        id: fileDialog
                        selectFolder: false
                        title: "Select Photo"
                        selectMultiple: false
                        nameFilters: ["*.png"]

                        onAccepted: {
                            console.log(fileUrl)
                            usaerProfileImg.source = fileUrl
							messageDialog.open()
                        }
                    }
			MessageDialog {
				id: messageDialog
				title: "May I have your attention please"
				text: "It's so cool that you are using Qt Quick."
				onAccepted: {
					console.log("And of course you could only agree.")
					Qt.quit()
				}
				//Component.onCompleted: visible = true
			}
					
			
			 
					
            Text {
                anchors.top: accountCapital.bottom
                anchors.horizontalCenter: accountCapital.horizontalCenter
                text: "LogOut"
				font.pointSize: 14
            }
        }
         

         Rectangle {
            id:accountRightRect
			y:100
			color:"transparent"
            anchors.left: accountLeft.right
            anchors.right:parent.right
            //anchors.top: parent.top
            height: parent.height* 0.6
            anchors.leftMargin: 20
            anchors.rightMargin: 20
            
            Text {
                id:userName
                anchors.right:parent.right
                anchors.top: parent.top
                text: "Hello <p style=color: #0000a0><b>" + "user" + "</b></p>"
            }
            Text {
                id:welcomeUser
                anchors.right:parent.right
                anchors.top: userName.bottom
                text: "<p>Welcome to VICI Print</p>"
            }
            Text {
                anchors.left:parent.left
                anchors.top: welcomeUser.bottom
                text: "<p>Email:</p>"
            }
            Text {
                id:userEmail
                anchors.right:parent.right
                anchors.top: welcomeUser.bottom
                text:"<p>" +  "emial" + "</p>"
            }
            Text {
                anchors.left:parent.left
                anchors.top: userEmail.bottom
                text: "<p>Password:</p>"
            }
            Text {
                id:userPassword
                anchors.right:parent.right
                anchors.top: userEmail.bottom
                text: "<p>********</p>"
            }
            Text {
                anchors.left:parent.left
                anchors.top: userPassword.bottom
                text: "<p>Default Printer:</p>"
            }
            Text {
                anchors.right:parent.right
                anchors.top: userPassword.bottom
                text: "Printer 123"
            }

        }//end of accountRightRect
        Image {
                id: iconSteps
                width: parent.width
                height: 240
                source: "Guide.png"
                fillMode: Image.PreserveAspectFit
                clip: true
                anchors.bottom: parent.bottom
                anchors.right: parent.right
                //anchors.left: parent.left
                anchors.margins: 10
				 mipmap: true
        }
		
		

     }//end of accountRect
	 
	 
 }

}