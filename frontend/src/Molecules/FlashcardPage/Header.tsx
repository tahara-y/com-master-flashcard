import styled from "@emotion/styled";
import HamburgerMenuItems from "../CommonPage/HamburgerMenuItems";

const Header = () => {
  return (
    <SHeader>
      <SLogin href="/menu">TOP</SLogin>
      <SHeaderText>
        <SHeaderTextSmall>.com master</SHeaderTextSmall>
        <SHeaderTextBig>ADVANCE</SHeaderTextBig>
      </SHeaderText>
      <SHamburgerMenuIcon>
        <HamburgerMenuItems />
      </SHamburgerMenuIcon>
    </SHeader>
  );
};

const SHeader = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  height: 3.75rem;
  margin-top: 2.75rem;
`;

const SLogin = styled.a`
  color: #38a169;
  position: absolute;
  left: 1rem;
  font-weight: 600;
`;

const SHeaderText = styled.div`
  font-weight: 600;
  display: flex;
  flex-direction: column;
  justify-content: center;
  position: relative;
`;

const SHeaderTextSmall = styled.div`
  align-items: center;
`;

const SHeaderTextBig = styled.div`
  display: flex;
  font-size: 1.5rem;
`;

const SHamburgerMenuIcon = styled.div`
  position: absolute;
  right: 1rem;
`;

export default Header;
