import xml.etree.ElementTree as ET
import random
from datetime import datetime
import os


a="""<?xml version='1.0' encoding='utf-8'?>
<Message xmlns="http://www.nri.com/igv">
<Header>
<Action>TRANSFER_IN</Action>
<CommunicationCode>REQUEST</CommunicationCode>
<CreationTime>20230104232931</CreationTime>
<MessageId>{VAL1}</MessageId>
<MessageType>Client</MessageType>
<SenderSystemId>CORETX</SenderSystemId>
<SenderEnterpriseId>AEX</SenderEnterpriseId>
<RecipientSystemId>IGV</RecipientSystemId>
</Header>
<Body>
<AccountType>Individual</AccountType>
<CSPAccountType>SPSD</CSPAccountType>
<AccountNumber>{VAL2}</AccountNumber>
<ShortName>GRYFFIN DIOR</ShortName>
<ResidencyIndicator>D</ResidencyIndicator>
<OwnershipType>SIGL</OwnershipType>
<InvestorType>I</InvestorType>
<OrderClass>FILL</OrderClass> 
<IsGSTExempt>N</IsGSTExempt>
<CHESSSponsorship>
<RegistrationDetails>
<AddressLines>6 JOWETT STREET</AddressLines>
<AddressLines>COOMERA QLD</AddressLines>
<AusPostCode>1440</AusPostCode>
<Country>AU</Country>
<TownName>ADDRESS</TownName>
<State>Victoria</State>
<Name>GRYFFIN DIOR</Name>
</RegistrationDetails>
<EmailAddress>
<Email>kuntald@nrifintech.com</Email>
<IsChessEmail>Y</IsChessEmail>
</EmailAddress>
<TelecomAddress>
<AddressType>Mobile</AddressType>
<Number>9715715197</Number>
</TelecomAddress>
<ClientReportingRequired>Y</ClientReportingRequired>
</CHESSSponsorship>
<AccountOpenedBy>CORETX_USER</AccountOpenedBy>
<Remarks>ENTRY</Remarks>
<HINTransferDetails>            
<BrokerPID>06382</BrokerPID>        
<HIN>{VAL3}</HIN>        
</HINTransferDetails>            
<HolderAttribute>
<Name>GRYFFIN DIOR</Name>
<InvestorType>I</InvestorType>
</HolderAttribute>
<AccountClass>B2B</AccountClass>
<AccountGleType>TPCL</AccountGleType>
<AccountServiceAttributes>
<AccountServiceAttribute>
<ServiceName>D-EQ-SP</ServiceName>
<ServiceAction>ENTRY</ServiceAction>
<Date>2023-04-27</Date>
</AccountServiceAttribute>
</AccountServiceAttributes>
<AdditionalCrossRefs>
<AccountCrossRef>
<AccountNumber>{VAL2}</AccountNumber>
<AccountNumberType>IRESS</AccountNumberType>
</AccountCrossRef>
<ClientCrossRef>
<ClientId>{VAL2}</ClientId>
<ClientIdType>CORETX</ClientIdType>
</ClientCrossRef>
</AdditionalCrossRefs>
<CustomerBlock>
<CustomerCodeCrossRef>
<CustomerCode>{VAL2}</CustomerCode>
<CustomerCodeType>ISTAR</CustomerCodeType>
</CustomerCodeCrossRef>
<CustomerName>GRYFFIN DIOR</CustomerName>
</CustomerBlock>
<AgentAdvisorBlock>
<AgentCode>000</AgentCode>
<DefaultAgent>Y</DefaultAgent>
<AdvisorBlock>
<AdvisorCode>000</AdvisorCode>
<AdvisorRole>Main</AdvisorRole>
</AdvisorBlock>
</AgentAdvisorBlock>
<CashBankDetails>
<CashBankDetail>
<BankAccountName>GRYFFIN DIOR</BankAccountName>
<BankAccountNumber>091302331</BankAccountNumber>
<BankCode>062-000</BankCode>
<BankCodeType>BSB</BankCodeType>
<Currency>AUD</Currency>
<MarketCode>AU</MarketCode>
<Priority>1</Priority>
<SettlementFor>SECURITY_TRADE</SettlementFor>
<WayOfPayment>DIRECT_ENTRY</WayOfPayment>
</CashBankDetail>
</CashBankDetails>
<ContractNotePreference>BOTH</ContractNotePreference>                                                    
<NettingPolicy>GROSS</NettingPolicy>
<AutoSecurityContra>NET</AutoSecurityContra>
<OneDayCashForward>Y</OneDayCashForward>
<OneDayCashRetain>Y</OneDayCashRetain>
<PaymentFrequency>DAILY</PaymentFrequency>
<RiskAssessment>10%</RiskAssessment>           
</Body>
<Footer>
<SendingTime>20230104232931</SendingTime>
</Footer>
</Message>"""
num=100000
hin=1000000000
output_directory = 'D:\\Tools\\ActiveMQSender\\messages'
print(datetime.now())
for i in range(1,5000):
    num=num+i
    hin=hin+i
    file_path = os.path.join(output_directory, f"xml_{num}.xml")
    x=a.replace("{VAL1}",f"A{num}").replace("{VAL2}",f"B{num}").replace("{VAL3}",f"{hin}")
    with open(file_path,'wt') as f:
        f.write(x)
print(datetime.now())

