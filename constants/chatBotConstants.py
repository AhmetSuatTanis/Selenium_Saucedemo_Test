giris_URL="https://tobeto.com/giris"
chatBot_Iframe_xpath="//iframe[@class='exw-launcher-frame animated bounce']"
chatBot_xpath="//*[@id='launcher']/div"
chatBotMessageBox_Iframe_xpath="//*[@id='exw-conversation-frame']"
messageInputBox_xpath="//*[@id='exw-conversation-frame-body']/div/div/div/div[3]/form/textarea"
messageText="Selam"
messageSendButton_xpath="//*[@id='exw-conversation-frame-body']/div/div/div/div[3]/form/div/button"
actualTitleOfMessageBox_xpath="//h4[contains(.,'Tobeto Yardım')]"
expectedTitleOfMessageBox="Tobeto Yardım"
expectedWelcomeMessage="Merhabalar, Tobeto'ya hoş geldiniz."
actualWelcomeMessage_xpath="//div[@id='exw-messages']/div/div/div/div/div/div/p"
nameInputBox_xpath="//*[@id='exw-messages']/div[3]/div[2]/div[2]/input"
name="Ahmet Tanış"
nameSendButton_CSS=".exw-inline-response-input-container > svg"
expectedGreetingMessage="Memnun oldum"
actualGreetingMessage_xpath="//*[@id='exw-messages']/div[4]/div/div/div/div[1]/div/div"
topicSelection_xpath="//*[@id='exw-messages']/div[4]/div/div/div/div[2]/div/div/div[1]"
expectedSelectionMessage="Tobeto; üniversite öğrencileri, profesyoneller, işini/mesleğini değiştirmek ya da işinde gelişmek isteyenler için eğitim ve gelişim platformudur."
actualSelectionMessage_xpath="//div[@class='exw-sender-response']/p[contains(text(),'Tobeto;')]"
topicSelection2_xpath="//div[@class='exw-reply'][contains(text(),'Eğitimlerimiz')]"
expectedEducationsMessage="Aşağıdaki konu başlıkları için sana yardımcı olabilirim."
actualEducationsMessage_xpath="//div[@class='exw-message-text']/div[contains(text(),'Aşağıdaki konu başlıkları için sana yardımcı olabilirim.')]"
topicSelection3_xpath="//*[@id='exw-messages']/div[8]/div/div/div/div[2]/div/div/div[1]"
actualEducationsList_xpath="//*[@id='exw-messages']/div[10]/div[1]/div/div"
expectedHelpMessage="Yardımcı olmamı istediğiniz başka bir konu var mı?"
actualHelpMessage_xpath="//div[@class='exw-message-text']/div[contains(text(),'Yardımcı')]"
yesButton_xpath="//div[@class='exw-replies']/div[contains(text(),'Evet')]"
noButton_xpath="//div[@class='exw-replies']/div[contains(text(),'Hayır')]"
actualLastResponseMessage_xpath="//div[@class='exw-sender-response']/p[contains(text(),'Sorun olursa her zaman burdayım')]"
expectedLastResponseMessage="Sorun olursa her zaman burdayım"







