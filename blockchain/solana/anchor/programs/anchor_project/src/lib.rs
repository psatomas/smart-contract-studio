use anchor_lang::prelude::*;

declare_id!("8oSMXsFzJ1udTRe38EQixhe3Z5NZgoRR4P4pg74y9Exa");

#[program]
pub mod anchor_project {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        msg!("Greetings from: {:?}", ctx.program_id);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize {}
