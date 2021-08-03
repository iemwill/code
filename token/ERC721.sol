// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.2.0/contracts/token/ERC721/ERC721.sol";

contract exampleNFT is ERC721 {
    address private owner;
    constructor() ERC721 ("Ex-NFT", "ENFT"){
        owner = msg.sender;
        _safeMint(owner, 0, "");
    }
    function mint(address to, uint256 tokenId, bytes memory data) public virtual {
        require(msg.sender == owner);
        _safeMint(to, tokenId, data);
    }
}