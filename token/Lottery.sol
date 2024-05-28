pragma solidity ^0.4.19;

/**
 * The Owned contract ensures that only the creator (deployer) of a 
 * contract can perform certain tasks.
 */
contract Owned {
	address public owner = msg.sender;
	event OwnerChanged(address indexed old, address indexed current);
	modifier only_owner { require(msg.sender == owner); _; }
	function setOwner(address _newOwner) only_owner public { OwnerChanged(owner, _newOwner); owner = _newOwner; }
}

contract Lottery is Owned {
	mapping (uint256 => mapping (address => uint256)) public lotteries;
	uint256 public lottery_Nr;
	mapping (address => uint256) public winners;
	uint256 public price;

	uint256 internal ID;
	// mapping (uint256 => address) public user_ID; need for the one below
	// mapping (address => uint256) internal check_ID; just for checking if someone is already in.
	mapping (uint256 => mapping (uint256  => address)) internal lottery_IDs;
		
	event Winner(address lottery_Winner, uint256 lottery_Number, uint256 value_won);
	event new_Bet(address address_from_bet, uint256 value);
	event new_lottery_started(bool start_of_new_lottery);
	event GO_given(bool spin_is_free);
	event New_Price(uint256 the_new_price);
			
	modifier correct_value() { if (msg.value != uint256(price)) revert(); _; }
	modifier check_bets() { if (ID < 10) revert(); _; }
			
	function Lottery () public { lottery_Nr = 0; ID = 0; price = 100000000000000000;}

	function new_lottery () internal { lottery_Nr += 1; ID = 0; new_lottery_started(true); }
	
	function new_price (uint256 _price) public only_owner() { price = _price; New_Price(_price); }
	
	function spin_the_wheel (uint256 _n) public check_bets() {
		address spin_winner;
		spin_winner = lottery_IDs[lottery_Nr][(uint256(keccak256(now)[_n]) % ID)];
		uint256 amount;
		amount = this.balance;
		Winner(spin_winner, lottery_Nr, amount);
		spin_winner.transfer(amount);
		new_lottery();
	}
	
	function () public payable correct_value() {
		lotteries[lottery_Nr][msg.sender] += msg.value;
		lottery_IDs[lottery_Nr][ID] = msg.sender;
		ID += 1;
		new_Bet(msg.sender, msg.value);
	}
	
	function chance_of (address bet_address) public view returns(uint256 bets, uint256 total_bets) { // need to be double
		return ((lotteries[lottery_Nr][bet_address] / uint256(price)), ID);
	}	
}
